from lab1.pessoa import Pessoa


class Funcionario(Pessoa):
    def __init__(self,nome,numero):
        self.numero = numero
        super().__init__(nome)
        
        
        
    def obter_numero (self):
        return self.numero 
