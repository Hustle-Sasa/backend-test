
from ..models.bonus_points import BonusPoints
from ..models.database import db


def redeem_referral_code(refferal_code_instance):

    # update points
    bonus_points = BonusPoints.query.filter_by(user_id=refferal_code_instance.user_id).first()
    if bonus_points:
        bonus_points.points += refferal_code_instance.points
    else:
        bonus_points = BonusPoints(user_id=refferal_code_instance.referee, points=10)

    db.session.add(bonus_points)
    db.session.commit()

    refferal_code_instance.is_active = False
    db.session.add(refferal_code_instance)
    db.session.commit()

