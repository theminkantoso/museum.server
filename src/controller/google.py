from datetime import datetime

from flask import url_for, jsonify
from flask_restful import Resource
from src.controller import oauth
from flask_jwt_extended import create_access_token

from src.models.accountDb import AccountDb


class Google(Resource):

    def get(self):
        google = oauth.create_client('google')
        redirected_uri = url_for('authorize', _external=True)
        return google.authorize_redirect(redirected_uri)


class GoogleLoginAuthorize(Resource):

    def get(self):
        google = oauth.create_client('google')  # create the google oauth client
        token = google.authorize_access_token()
        resp = google.get('userinfo').json()
        account = AccountDb.find_by_email(resp['email'])
        if account is not None:
            access_token = create_access_token(identity=resp['email'].lower())
            return jsonify(access_token=access_token, role=0)
        else:
            account_create = AccountDb(email=resp['email'].lower(), password=None, RoleId=0, isActivated=1,
                                       confirmedAt=datetime.now(), GoogleId=resp['id'], CreateAt=datetime.now(),
                                       updatedAt=datetime.now())
            account_create.save_to_db()
            access_token = create_access_token(identity=resp['email'].lower())
            return jsonify(access_token=access_token, role=0)

