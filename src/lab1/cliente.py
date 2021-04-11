from lab1.fatura import Fatura

from lab1.pessoa import Pessoa

class Cliente(Pessoa):
    def __init__(self,nome, numero):
        self.numero = numero
        self.faturas = []
        super().__init__(nome)
        
        
    def obter_numero (self):
        return self.numero
    
    def obter_fatura(self):
        return self.fatura
    
