from flask_restful import Resource
from flask import request

from exercicio_api.dao.pessoa_dao import AmigosDao
from exercicio_api.model.pessoa_model import AmigosModel

class AmigosController(Resource):
    def __init__(self):
        self.dao = AmigosDao()

    def get(self, id=None):
        if id:
            return self.dao.get_by_id(id)
        return self.dao.list_all()


    def post(self):
        nome = request.json['nome']
        sobrenome = request.json['sobrenome']
        idade = int(request.json['idade'])
        pessoa = PessoaModel(nome, sobrenome, idade)
        msg = self.dao.insert(pessoa)
        return msg

    def put(self, id):
        nome = request.json['nome']
        sobrenome = request.json['sobrenome']
        idade = int(request.json['idade'])
        pessoa = AmigosModel(nome, sobrenome, idade, id)
        msg = self.dao.update(pessoa)
        return msg

    def delete(self, id):
        return self.dao.remove(id)