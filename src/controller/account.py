import os

from flask_restful import Resource, reqparse
from src.models.accountDb import AccountDb, RevokedTokenModel
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime
from itsdangerous import URLSafeTimedSerializer, SignatureExpired
from src.controller import my_mail
from flask import url_for, jsonify
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity, get_jwt
from flask_mail import Message

from src.services.accountService import AccountService

su = URLSafeTimedSerializer('Thisisasecret!')  # reformat later


class Account(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('email', type=str)
    parser.add_argument('password', type=str)

    def get(self):
        # print(OrderDb.stats_order_by_date('2021-12-12T17:42:51.386Z'))
        str = '2021-12-12T17:42:51.386Z'
        print(str[0:10])
        # print(StatisticsService.stats_ticket_all())
        pass

    def post(self):
        data = Account.parser.parse_args()
        email = data['email']
        password = data['password']
        regex_mail = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
        if not AccountService.validate_regex(email.lower(), regex_mail) or not password.isalnum():
            return {'msg': "Sai tài khoản hoặc mật khẩu"}, 400
        if AccountDb.find_by_email(email.lower()) is None:
            return {'msg': "Sai tài khoản hoặc mật khẩu"}, 401
        user = AccountDb.find_by_email(email.lower())
        if check_password_hash(user.Password, password):
            if user.isActivated:
                access_token = create_access_token(identity=email.lower())
                return jsonify(access_token=access_token, role=user.RoleId)
            else:
                return {"msg": "Hãy xác nhận tài khoản qua hộp mail của bạn"}, 401
        return {"msg": "Sai tài khoản hoặc mật khẩu"}, 401

    def delete(self):
        return {'msg': 'Not allowed'}, 404

    def put(self):
        return {'msg': 'Not allowed'}, 404


class Register(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('email', type=str)
    parser.add_argument('password', type=str)

    def get(self):
        pass

    def post(self):
        data = Register.parser.parse_args()
        email = data['email']
        password = data['password']
        regex_mail = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
        if not AccountService.validate_regex(email.lower(), regex_mail) or not password.isalnum():
            return {'msg': "Sai tài khoản hoặc mật khẩu"}, 400
        if AccountDb.find_by_email(email.lower()) is not None:
            return {'msg': "Tài khoản đã tồn tại"}, 400
        user = AccountDb(email=email.lower(), password=generate_password_hash(password, method='sha256'), RoleId=1,
                         isActivated=0, confirmedAt=None, GoogleId=None, CreateAt=datetime.now(), updatedAt=None)
        token = su.dumps(email.lower(), salt='email-confirm')
        link = url_for('confirmation', token=token, _external=False)
        try:
            msg = Message('Confirm Email', sender=os.environ.get('MAIL'), recipients=[email.lower()])
            msg.body = 'Click vào link http://127.0.0.1:5000{}'.format(link)
            my_mail.send(msg)
            user.save_to_db()
        except Exception as e:
            print(e)
            return {'msg': "Lỗi không thể gửi mail xác nhận"}, 400
        return {'msg': "Đăng ký thành công"}, 200

    def delete(self):
        return {'msg': 'Not allowed'}, 404

    def put(self):
        return {'msg': 'Not allowed'}, 404


class Confirmation(Resource):
    def get(self, token):
        try:
            email = su.loads(token, salt='email-confirm', max_age=3600)
            get_user = AccountDb.find_by_email(email)
            get_user.isActivated = 1
            get_user.confirmedAt = datetime.now()
            get_user.updatedAt = datetime.now()
            get_user.commit_to_db()
        except SignatureExpired:
            return {'msg': "Hết hạn"}, 400
        return {'msg': "Kích hoạt thành công"}, 200


class Repass(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('email', type=str)

    def post(self):
        data = Repass.parser.parse_args()
        email = data['email']
        regex_mail = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
        if not AccountService.validate_regex(email.lower(), regex_mail):
            return {'msg': "Mail sai định dạng"}, 400
        if AccountDb.find_by_email(email.lower()) is None:
            return {'msg': "Tài khoản không tồn tại"}, 400
        try:
            get_user = AccountDb.find_by_email(email)
            new_password = AccountService.random_string()
            get_user.Password = generate_password_hash(new_password, method='sha256')
            msg = Message('Mật khẩu khôi phục', sender=os.environ.get('MAIL'), recipients=[email.lower()])
            msg.body = 'Mật khẩu mới của bạn là {}'.format(new_password)
            my_mail.send(msg)
            get_user.updatedAt = datetime.now()
            get_user.commit_to_db()
        except:
            return {'msg': "Không thể gửi mail xác nhận"}, 400
        return {'msg': "Mật khẩu mới đã được gửi về mail của bạn!"}, 200


class ChangePass(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('password', type=str)
    parser.add_argument('newpassword', type=str)
    parser.add_argument('renewpassword', type=str)

    @jwt_required()
    def post(self):
        data = ChangePass.parser.parse_args()
        password = data['password']
        new_password = data['newpassword']
        re_new_password = data['renewpassword']
        if new_password != re_new_password:
            return {'msg': "Nhập lại mật khẩu không khớp"}, 400
        email = get_jwt_identity()
        get_user = AccountDb.find_by_email(email)
        if check_password_hash(get_user.Password, password):
            get_user.Password = generate_password_hash(new_password, method='sha256')
            get_user.updatedAt = datetime.now()
            get_user.commit_to_db()
            return {'msg': "Lưu mật khẩu mới thành công"}, 200
        return {'msg': "Sai mật khẩu"}, 400


class UserLogoutAccess(Resource):
    """
    User Logout Api
    """

    @jwt_required()
    def post(self):
        jti = get_jwt()['jti']
        try:
            # Revoking access token
            revoked_token = RevokedTokenModel(jti=jti)

            revoked_token.add()

            return {'msg': 'Access token has been revoked'}, 200

        except:

            return {'msg': 'Something went wrong'}, 500







