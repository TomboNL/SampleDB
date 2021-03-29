from flask_restful import reqparse

class ParserFactory:
    def getCategoryParser(self):
        parser = reqparse.RequestParser()
        parser.add_argument('category_id', type=int)
        parser.add_argument('name')
        parser.add_argument('last_update')
        return parser
