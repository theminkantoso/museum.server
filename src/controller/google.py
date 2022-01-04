from datetime import datetime

from flask import jsonify
from flask_restful import Resource, reqparse
from flask_jwt_extended import create_access_token

from src.models.accountDb import AccountDb


class Google(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('email', type=str)
    parser.add_argument('googleId', type=str)

    # def get(self):
    #     google = oauth.create_client('google')
    #     redirected_uri = url_for('authorize', _external=True)
    #     return google.authorize_redirect(redirected_uri)

    def post(self):
        data = Google.parser.parse_args()
        email = data['email']
        googleId = data['googleId']
        account = AccountDb.find_by_email(email)
        if account is not None:
            if account.GoogleId is None:
                account.GoogleId = googleId
                account.commit_to_db()
            access_token = create_access_token(identity=email.lower())
            return jsonify(access_token=access_token, role=1)
        else:
            account_create = AccountDb(email=email.lower(), password=None, RoleId=1, isActivated=1,
                                       confirmedAt=datetime.now(), GoogleId=googleId, CreateAt=datetime.now(),
                                       updatedAt=datetime.now())
            account_create.save_to_db()
            access_token = create_access_token(identity=email.lower())
            return jsonify(access_token=access_token, role=1)


# class GoogleLoginAuthorize(Resource):
#
#     def get(self):
#         google = oauth.create_client('google')  # create the google oauth client
#         token = google.authorize_access_token()
#         resp = google.get('userinfo').json()
#         account = AccountDb.find_by_email(resp['email'])
#         if account is not None:
#             if account.GoogleId is None:
#                 account.GoogleId = resp['id']
#                 account.commit_to_db()
#             access_token = create_access_token(identity=resp['email'].lower())
#             return jsonify(access_token=access_token, role=0)
#         else:
#             account_create = AccountDb(email=resp['email'].lower(), password=None, RoleId=1, isActivated=1,
#                                        confirmedAt=datetime.now(), GoogleId=resp['id'], CreateAt=datetime.now(),
#                                        updatedAt=datetime.now())
#             account_create.save_to_db()
#             access_token = create_access_token(identity=resp['email'].lower())
#             return jsonify(access_token=access_token, role=1)

