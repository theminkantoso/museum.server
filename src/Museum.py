from flask_restful import Api
from flask import Flask
from database import db

from controller.images import image, Images
from controller.artifact import artifact, artifacts
from controller.museumevent import Event, Events
from controller.souvenir import souvenir, souvenirs
from controller.artifacttype import artifactType, artifactTypes
from src.controller.account import Account, Register, Confirmation, Repass, ChangePass, UserLogoutAccess
from src.controller.orderTicket import Order, OrderQR

from controller.artifacttypemapping import artifactTypeMapping, artifactTypeMappings, artifactsType
from controller.accountfavoriteartifact import accountFA, accountFAs
from controller.rattings import Rattings, ratting
from controller.notification import notification, Notifications
from src import controller


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:''@localhost/museum'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config.from_pyfile('core/config.py')

api = Api(app)
controller.init_app(app)

api.add_resource(image, '/image/<int:id>',  '/image')
api.add_resource(Images, '/images')

api.add_resource(artifact, '/artifact/<string:name>', '/artifact')
api.add_resource(artifacts, '/artifacts')

api.add_resource(Event, '/event/<string:name>', '/event')
api.add_resource(Events, '/events')

api.add_resource(souvenir, '/souvenir/<string:name>', '/souvenir')
api.add_resource(souvenirs, '/souvenirs')

api.add_resource(artifactType, '/artifactType/<string:name>', '/artifactType')
api.add_resource(artifactTypes, '/artifactTypes')

api.add_resource(Account, '/login')
api.add_resource(Register, '/register')
api.add_resource(Confirmation, '/confirm_email/<token>')
api.add_resource(Repass, '/repass')
api.add_resource(ChangePass, '/changepass')
api.add_resource(UserLogoutAccess, '/logout')

api.add_resource(Rattings, '/rattings')
api.add_resource(ratting, '/ratting/<int:id>', '/ratting')

api.add_resource(Notifications, '/notifications')
api.add_resource(notification, '/notification/<int:id>', '/notification')

api.add_resource(artifactTypeMapping, '/artifactTypeMapping/<int:id>&<int:typeId>', '/artifactTypeMapping')
api.add_resource(artifactTypeMappings, '/artifactTypeMappings')
api.add_resource(artifactsType, '/artifactsType/<int:id>')

#accountFavoriteArtifact
api.add_resource(accountFA, '/accountFA/<int:AccId>&<int:id>', '/accountFA')
api.add_resource(accountFAs, '/accountFAs/<int:AccId>') # phân loại theo account

api.add_resource(Order, '/orderticker/<int:id>')
api.add_resource(OrderQR, '/checkorder')

# flask_jwt_extended == 3.21.0
# @controller.jwt_manager.token_in_blacklist_loader
# def check_if_token_in_blacklist(decrypted_token):
#
#     jti = decrypted_token['jti']
#
#     return controller.account.RevokedTokenModel.is_jti_blacklisted(jti)

@controller.jwt_manager.token_in_blocklist_loader
def check_if_token_revoked(jwt_header, jwt_payload):
    jti = jwt_payload["jti"]
    token = db.session.query(controller.account.RevokedTokenModel.id).filter_by(jti=jti).scalar()
    return token is not None


if __name__ == '__main__':
    db.init_app(app)
    app.run(debug=True)

