# System imports
import enum
from sqlalchemy import event
from sqlalchemy.orm import object_session

from .database import db
from .base_model import BaseModel



class User(BaseModel):
    """"Class for user db table"""

    __tablename__ = 'user'

    user_id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)
    phone = db.Column(db.Integer, nullable=True)
    email = db.Column(db.String(60), nullable=False, unique=True)
    token = db.Column(db.String(100), nullable=False, unique=True)

    def get_child_relationships(self):

        """Method to get all child relationships a model has. Overide in the
        subclass if the model has child models.
        """
        return None

    def __repr__(self):
        return f'<User {self.first_name}>'

# @event.listens_for(User, 'before_insert')
# def generate_referral_codes(mapper, connect, target):
#     """Function that generates referral codes for a user
#     Args:
#         mapper: SQLAlchemy mapper
#         connect: SQLAlchemy connection
#         target: SQLAlchemy target
#     Returns:
#         None
#     """
#     import pdb;pdb.set_trace()
    # object_session(target).add(ReferralCode(
    #         referral_code=generate_referral_code(),
    #         referee = target
    #     ))
    # @event.listens_for(Session, "after_flush", once=True)
    # def receive_after_flush(session, context):
    #     session.add(ReferralCode(
    #         referral_code=generate_referral_code(),
    #         referee = target
    #     ))
    # save_referral_codes(target)