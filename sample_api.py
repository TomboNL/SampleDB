from flask import Flask, jsonify
from flask_restful import reqparse, abort, Api, Resource
from flask_restful import fields, marshal_with
from flask_cors import CORS, cross_origin
from parserfactory import ParserFactory
from db_handler import DB_handler
from category import Category
import json

app = Flask(__name__)
api = Api(app)
cors = CORS(app)

handler = DB_handler()
parse_factory = ParserFactory()

category_fields = {
    "category_id": fields.Integer,
    "name": fields.String,
    "last_update": fields.DateTime
}

# CategoryList
class CategoryList(Resource):
    @marshal_with(category_fields)
    def get(self):
        parser = parse_factory.getCategoryParser()
        args = parser.parse_args()
        if (args['category_id'] == -1):
            return handler.getCategoryList()
        else:
            return handler.getCategory(args['category_id'])

    def post(self):
        parser = parse_factory.getCategoryParser()
        args = parser.parse_args()
        new_cat = Category()
        new_cat.category_id = args['category_id']
        new_cat.name = args['name']
        new_cat.last_update = args['last_update']
        print(new_cat)
        handler.addCategory(new_cat)

##
## Actually setup the Api resource routing here
##
api.add_resource(CategoryList, '/categories')


if __name__ == '__main__':
    app.run(debug=True)