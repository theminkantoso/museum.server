import os

from flask import request
from flask_restful import Resource, reqparse
from src.models.imageDb import Image
from werkzeug.utils import secure_filename
from src.statics import APP_ROOT


class image(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('ImageId', type=int)
    parser.add_argument('Name', type=str)
    parser.add_argument('Content', type=str)
    parser.add_argument('Url', type=str)
    parser.add_argument('Path', type=str)
    parser.add_argument('MimeType', type=str)

    def get(self, id):
        img = Image.find_by_id(id)
        if img:
            # print(img.Url)
            # s = str(img.Url)
            # print(type(s))
            # b = sqlalchemy.BINARY(s)
            # print(type(b))
            # return Response(img.Url, mimetype=img.MimeType)
            return img.json()
        return {'message': 'Image not found'}, 404

    def post(self):
        pic = request.files['pic']
        if not pic:
            return {'message': 'No pic loader'}, 400
        filename = secure_filename(pic.filename)
        mimetype = pic.mimetype
        url = filename
        path = 'statics/images/' + filename

        if Image.find_by_name(filename):
            return {'message': "An image with name '{}' already exists.".format(filename)}, 400
        # img = Image(Name=filename, Content='', Url=pic.read(), Path='', MimeType=mimetype)
        pic.save(os.path.join(APP_ROOT, filename))
        img = Image(Name=filename, Content='', Url=url, Path=path, MimeType=mimetype)
        try:
            img.save_to_db()
        except:
            return {"message": "An error occurred inserting the image."}, 500
        img = Image.find_by_name(filename)
        return {'msg': 'Image added.', 'ImageId': img.ImageId}, 200

    def delete(self, id):
        img = Image.find_by_id(id)
        if img:
            img.delete_from_db()
            return {'message': 'Image deleted.'}
        return {'msg': 'Image not found.'}, 404

    def put(self, id):
        data = image.parser.parse_args()
        img = Image.find_by_id(id)
        if img:
            img.Name = data['Name']
            img.Content = data['Content']
            img.Url = data['Url']
            img.Path = data['Path']
            img.save_to_db()
            return {'message': 'Image put'}
        return {'message': 'Image not found.'}, 404


class Images(Resource):
    def get(self):
        return {'images': list(map(lambda x: x.json(), Image.query.all()))}
