from lab1.fatura import Fatura
from lab1.pessoa import Pessoa
from lab1.funcionario import Funcionario


class Vendedor(Funcionario,Pessoa):
    def __init__(self,fatura,numero):
        self.fatura= []
        super().__init__(numero)
        
        
        
    def obter_faturas (self):
        return self.fatura.append
    
    def obter_faturas(self,iniciodata,fimdata):
        return self.iniciodata,fimdata
