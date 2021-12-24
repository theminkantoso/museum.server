from flask import jsonify
from flask_restful import Resource, reqparse
from src.models.rattingsDb import Ratting


class ratting(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('RattingId', type=int)
    parser.add_argument('Star', type=float)
    parser.add_argument('Description', type=str)
    parser.add_argument('AccountId', type=int)

    # ratting get by user
    def get(self, id):
        data = Ratting.find_by_AccountId(id)
        if data:
            return data.json()
        return {'message': 'not found'}, 404

    # xem lai cho nay, error 
    # AccountId phải đã có trong bảng Account
    def post(self):
        data = ratting.parser.parse_args()
        if Ratting.find_by_AccountId(data.get('AccountId')):
            return {'message': "An user with id '{}' already exists.".format(data.get('AccountId'))}, 400
        if (data['Star'] < 0.0) or (data['Star'] > 5.0) :
            return {'message': 'Star ko hop le'}
        r = Ratting(**data)
        try:
            r.save_to_db()
            return r.json(), 201
        except:
            return {"message": "error."}, 500

    def delete(self, id):
        # tim va xoa danh gia theo id cua nguoi dung.
        r = Ratting.find_by_AccountId(id)
        if r:
            r.delete_from_db()
            return {'message': 'ratting deleted.'}
        return {'message': 'ratting not found.'}, 404

    def put(self, id):
        # nguoi dung sua doi danh gia, tim kiem danh gia dua tren accountid cua nguoi dung
        data = ratting.parser.parse_args()
        r = Ratting.find_by_AccountId(id)
        if (data['Star'] < 0.0) or (data['Star'] > 5.0) :
            return {'message': 'Star ko hop le'}
        if r:
            # r.RattingId = data['RattingId']
            # người dùng nhập đánh giá, hệ thống tự dộng cấp id.
            r.Star = data['Star']
            r.Description = data['Description']
            r.save_to_db()
            return r.json()
        return {'message': 'ratting not found.'}, 404


class Rattings(Resource):
    def get(self):
        data = {'rattings': list(map(lambda x: x.json(), Ratting.query.all()))}
        return data
