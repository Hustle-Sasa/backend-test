# System imports
import enum


from .database import db
from .base_model import BaseModel
from ..models.user import User

class ReferralCode(BaseModel):
    """"Class for user db table"""

    __tablename__ = 'referralcode'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(
        db.Integer,
        db.ForeignKey(User.user_id, ondelete='CASCADE'),
        nullable=True)

    referee = db.Column(
        db.Integer,
        db.ForeignKey(User.user_id, ondelete='CASCADE'),
        nullable=True)
    referral_code =  db.Column(db.Integer)
    is_active = db.Column(db.Boolean, default=True)

    def get_child_relationships(self):

        """Method to get all child relationships a model has. Overide in the
        subclass if the model has child models.
        """
        return None

    def __repr__(self):
        return f'<ReferralCode {self.referral_code}>'