from datetime import date, datetime
from flask import Blueprint
from api.models.referral_code import ReferralCode
from flask_restx import Resource
from sqlalchemy.exc import IntegrityError
import csv

from main import api

from ..models.database import db
from ..models import User
from ..helpers.date_formatter import date_formatter
from ..helpers.generate_code import referral_code_instance
from ..helpers.redeem_code import redeem_referral_code

auth_namespace = api.namespace(
    'users',
    description="A collection of User related endpoints"
)


@auth_namespace.route("/redeem/<string:referral_code>")
class CodeRedeemResource(Resource):
    def get(self, referral_code):
        referral_instance = ReferralCode.query.filter_by(referral_code=referral_code).first()

        if not referral_instance:
            return  {"message": "Invalid referral code"}, 404
        if not referral_instance.is_active:
            return {"message": "Referral code already redeemed"}, 400

        referral_code_date = referral_instance.created_at
        curr_date = datetime.now()
        date_diff = curr_date - referral_code_date
        if date_diff.days > 2:
            return {"message": "Referral code expired"}, 400

        redeem_referral_code(referral_instance)

        return {"message": "Referral code redeemed successfully"}, 201


@auth_namespace.route("/migrate")
class UserMigrateResource(Resource):
    def get(self):
        try:
            csv_file_path = 'Dummy data - Sheet1.csv'
            csv_reader = csv.reader(open(csv_file_path, 'r'))
            next(csv_reader)


            for row in csv_reader:
                new_user = User(
                    user_id=row[0],
                    first_name=row[1],
                    last_name=row[2],
                    phone=row[3],
                    email=row[4],
                    token=row[5],
                    created_at=date_formatter(row[6]),
                    updated_at=date_formatter(row[7]),
                )


                db.session.add(new_user)
                db.session.commit()

                new_code = referral_code_instance(new_user)
                db.session.add(new_code)
                db.session.commit()

        except IntegrityError as e:
            # Iam using pass here because I don't
            # want the whole transaction to fail
            pass
        return {'message': 'Data migrated successfully'}, 201