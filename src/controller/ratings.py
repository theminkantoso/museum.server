import re
from flask_jwt_extended import get_jwt_identity, jwt_required
from flask_restful import Resource, reqparse
from src.models.ratingsDb import Rating

regex_id = '^[0-9]*$'


def validate_regex(input_string, regex):
    pattern = re.compile(regex)
    if pattern.fullmatch(input_string):
        return True
    return False


class rating(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('Star', type=int)
    parser.add_argument('Description', type=str)

    # rating get by user
    # @jwt_required()
    def get(self):
        # id_acc = get_jwt_identity()
        id_acc = 1
        data = Rating.find_by_AccountId(id_acc)
        if data:
            return data.json(), 200
        return {"Account has not rated yet"}

    # AccountId phải đã có trong bảng Account
    # @jwt_required()
    def post(self):
        data = rating.parser.parse_args()
        # id_acc = get_jwt_identity()
        id_acc = 3
        if Rating.find_by_AccountId(id_acc):
            return {'message': "An user with id '{}' already exists in ratings.".format(data.get('AccountId'))}, 400
        if (data['Star'] < 0) or (data['Star'] > 5):
            return {'message': 'Star ko hop le'}
        r = Rating(Star=data['Star'], Description=data["Description"], AccountId=id_acc)
        try:
            r.save_to_db()
            return {"message": "Rating added"}, 200
        except Exception as e:
            print(e)
            return {"message": "An error occurred inserting the rating."}, 500

    # @jwt_required()
    def delete(self):
        # id_acc = get_jwt_identity()
        id_acc = 1
        # tim va xoa danh gia theo id cua nguoi dung.
        r = Rating.find_by_AccountId(id_acc)
        if r:
            try:
                r.delete_from_db()
                return {'message': 'rating deleted.'}, 200
            except:
                return {"message": "An error occurred deleting the rating."}, 500
        return {'message': 'Account has not rated yet'}, 404

    # @jwt_required()
    def put(self):
        # id_acc = get_jwt_identity()
        id_acc = 1
        # nguoi dung sua doi danh gia, tim kiem danh gia dua tren accountId cua nguoi dung
        data = rating.parser.parse_args()
        r = Rating.find_by_AccountId(id_acc)
        if (data['Star'] < 0) or (data['Star'] > 5):
            return {'message': 'Star ko hop le'}, 400
        if r:
            try:
                r.Star = data['Star']
                r.Description = data['Description']
                r.save_to_db()
                return {"message": "rating updated"}, 200
            except:
                return {"message": "An error occurred updating the rating."}, 500
        return {'message': 'Account has not rated yet'}, 404


class Ratings(Resource):
    def get(self):
        average = str(Rating.average())
        data = {'average': average, 'ratings': list(map(lambda x: x.json(), Rating.query.all()))}
        return data, 200
