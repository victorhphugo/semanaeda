class Pessoas():
    def __init__(self,nome,idade):
        self.nome = nome
        self.idade = idade
    def pega_nome(self):
        return self.nome
    def dobro_idade(self):
        self.idade * 2
        return self.idade
    
pessoa = Pessoas("joao",20)
pessoa.pega_nome()