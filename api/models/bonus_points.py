# System imports
import enum


from .database import db
from .base_model import BaseModel
from . import User

class BonusPoints(BaseModel):
    """"Class for user db table"""

    __tablename__ = 'points'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(
        db.Integer,
        db.ForeignKey('user.user_id', ondelete='CASCADE'),
        nullable=False)

    points =  db.Column(db.Float)

    def get_child_relationships(self):

        """Method to get all child relationships a model has. Overide in the
        subclass if the model has child models.
        """
        return None

    def __repr__(self):
        return f'<User {self.name}>'