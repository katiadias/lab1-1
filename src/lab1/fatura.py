from lab1.data import Data
from lab1.vendedor import Vendedor
from lab1.cliente import Cliente
from lab1.item import Item




class Fatura():
    def __init__(self,numero,data,cliente,vendedor,item):
        self.numero = numero
        self.data = data
        self.cliente = cliente
        self.vendedor = vendedor
        self.item = []

        
        
    def obter_numero (self):
        return self.numero
    
    def obter_data (self):
        return self.data
    def obter_cliente (self):
        return self.cliente
    def obter_vendedor (self):
        return self.vendedor
    def obter_itens (self):
        return self.item
