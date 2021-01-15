from flask_restful import Resource
from flask_restful import reqparse

class HelloResource(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('idade', type=str, required=True, help='O campo idade é obrigatório')
    
    def get(self, name):
        message = f'Hello {name}'
        return {"message": message}
    
    def post(self, name):
        data = HelloResource.parser.parse_args()
        idade = data['idade']
        return {"message": f'Olá {name}, você informou que tem {idade} anos'}