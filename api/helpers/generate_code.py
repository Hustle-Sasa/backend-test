
import random

from ..models.referral_code import ReferralCode
from ..models.database import db


# generate random 6 integer codes
def generate_referral_code():
    """Function to generate referral code
    Args:
        None
    Returns:
        str -- referral code
    """

    code = ''
    for i in range(6):
        code += str(random.randint(0, 9))
    return int(code)


def referral_code_instance(user):
    """Function to save referral codes to database
    Arguments:
        user {User} -- User object
    Returns:
    """
    new_code = ReferralCode(
        referral_code=generate_referral_code(),
        referee = user.user_id
    )
    return new_code


