from datetime import datetime, timedelta
import pytest
import json

from main import create_app, db
from config import AppConfig
from api.models.referral_code import ReferralCode



@pytest.fixture(scope='module')
def test_client():
    app = create_app(AppConfig)
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.init_app(app)

    # Create a test client using the Flask application configured for testing
    with app.test_client() as testing_client:
        # Establish an application context
        with app.app_context():
            db.create_all()
            yield testing_client
            db.session.remove()
            db.drop_all()


class TestMigrateData:
    def test_migrate_user_data_succeeds(self, test_client):
        response = test_client.get('api/v1/users/migrate',content_type='application/json')
        data = json.loads(response.data.decode())
        assert response.status_code == 201
        assert data['message'] == 'Data migrated successfully'


class TestRedeemCodes:
    def test_redeem_points_succeeds(self,test_client):
        """Test to redeem bonus points"""
        referral_code = ReferralCode.query.all()[0]
        response = test_client.get(f'api/v1/users/redeem/{referral_code.referral_code}')
        data = json.loads(response.data.decode())
        assert response.status_code == 201
        assert data['message'] == 'Referral code redeemed successfully'

    def test_redeem_points_with_invalid_code_fails(self,test_client):
        """Test to redeem bonus points with invalid code"""
        response = test_client.get(f'api/v1/users/redeem/123221')
        data = json.loads(response.data.decode())
        assert data['message'] == 'Invalid referral code'
        assert response.status_code == 404

    def test_redeem_points_with_used_code_fails(self,test_client):
        """Test to redeem bonus points with used code"""
        referral_code = ReferralCode.query.all()[0]
        response = test_client.get(f'api/v1/users/redeem/{referral_code.referral_code}')
        response = test_client.get(f'api/v1/users/redeem/{referral_code.referral_code}')
        data = json.loads(response.data.decode())
        assert response.status_code == 400
        assert data['message'] == 'Referral code already redeemed'

    def test_redeem_points_with_expired_code_fails(self,test_client):
        """ Test to redeem bonus points with expired code"""
        referral_code = ReferralCode.query.all()[0]
        referral_code.created_at = datetime.now() - timedelta(days=3)
        response = test_client.get(f'api/v1/users/redeem/{referral_code.referral_code}',content_type='application/json')
        data = json.loads(response.data.decode())
        assert response.status_code == 400
        assert data['message'] == 'Referral code expired'