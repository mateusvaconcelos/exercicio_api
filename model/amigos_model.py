
class PessoaModel:
    def __init__(self, nome, sobrenome, idade, id=0):
        self.id = id
        self.nome = nome
        self.sobrenome = sobrenome
        self.idade = idade