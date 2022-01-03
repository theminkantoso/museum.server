from flask_jwt_extended import jwt_required, get_jwt_identity
from functools import wraps
from ..models.accountDb import AccountDb


@jwt_required()
def get_email_from_jwt_token():
    email = get_jwt_identity()
    return email


def admin_required(func):
    @wraps(func)
    def decorated(*args, **kwargs):
        try:
            user_email = get_email_from_jwt_token()
            user = AccountDb.find_by_email(user_email)
            if user.RoleId != 0:
                raise Exception()
        except:
            return {'msg': "You are not authorized to edit"}, 403
        return func(*args, **kwargs)
    return decorated
