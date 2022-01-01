from flask_restful import Api
from flask import Flask, url_for
from database import db

from controller.images import image, Images
from controller.artifact import artifact, artifacts
from controller.museumevent import Event, Events
from controller.souvenir import souvenir, souvenirs
from controller.artifacttype import artifactType, artifactTypes
from src.controller.account import Account, Register, Confirmation, Repass, ChangePass, UserLogoutAccess
from src.controller.orderTicket import OrderTicket, OrderQR, TicketOrders, TicketOrdersId
from src.controller.order_souvenir import OrderSouvenir, SouvenirOrders, SouvenirOrdersId
from src.controller.google import Google, GoogleLoginAuthorize

from controller.artifacttypemapping import artifactTypeMapping, artifactTypeMappings, artifactsType
from controller.accountfavoriteartifact import accountFA, accountFAs
from controller.ratings import Ratings, rating
from controller.notification import notification, Notifications, NotificationsAll
from src import controller

app = Flask(__name__, static_url_path='', static_folder='')
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:''@localhost/museum'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config.from_pyfile('core/config.py')

api = Api(app)
controller.init_app(app)

api.add_resource(image, '/image/<int:id>', '/image')
api.add_resource(Images, '/images')

api.add_resource(artifact, '/artifact/<int:id>', '/artifact')
api.add_resource(artifacts, '/artifacts')

api.add_resource(Event, '/event/<int:id>', '/event')
api.add_resource(Events, '/events')

api.add_resource(souvenir, '/souvenir/<int:id>', '/souvenir')
api.add_resource(souvenirs, '/souvenirs')

api.add_resource(artifactType, '/artifactType/<int:id>', '/artifactType')
api.add_resource(artifactTypes, '/artifactTypes')

api.add_resource(Account, '/login')
api.add_resource(Register, '/register')
api.add_resource(Confirmation, '/confirm_email/<token>')
api.add_resource(Repass, '/repass')
api.add_resource(ChangePass, '/changepass')
api.add_resource(UserLogoutAccess, '/logout')

api.add_resource(Ratings, '/ratings')
api.add_resource(rating, '/rating')

api.add_resource(Notifications, '/notifications')
api.add_resource(notification, '/notification/<int:Id>', '/notification')
api.add_resource(NotificationsAll, '/notificationsAll')

api.add_resource(artifactTypeMapping, '/artifactTypeMapping/<int:id>&<int:typeId>', '/artifactTypeMapping')
api.add_resource(artifactTypeMappings, '/artifactTypeMappings')
api.add_resource(artifactsType, '/artifactsType/<int:id>')

# accountFavoriteArtifact
api.add_resource(accountFA, '/accountFA/<int:AccId>&<int:id>', '/accountFA')
api.add_resource(accountFAs, '/accountFAs/<int:AccId>')  # phân loại theo account

api.add_resource(OrderTicket, '/orderticket')
api.add_resource(OrderQR, '/checkorder')
api.add_resource(TicketOrders, '/ticketorders')
api.add_resource(TicketOrdersId, '/ticketorders/<int:id>')
api.add_resource(OrderSouvenir, '/souvenirorder')
api.add_resource(SouvenirOrders, '/souvenirorders')
api.add_resource(SouvenirOrdersId, '/souvenirorders/<int:id>')

api.add_resource(Google, '/google')
api.add_resource(GoogleLoginAuthorize, '/authorize', endpoint="authorize")


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
