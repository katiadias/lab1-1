from lab1.gestor import Gestor
from lab1.vendedor import Vendedor
from lab1.cliente import Cliente
from lab1.item import Item
from lab1.data import Data

class Loja:
    def __init__(self,gestor,vendedor,cliente,item):
        self.gestor= []
        self.vendedor = []
        self.cliente = []
        self.item = []
        
#Retorna o gestor da loja.Quando a loja é criada, este objeto não existe.        
def obter_gestor(self) -> Gestor:
    return self.gestor

#Retorna a lista de objetos Vendedor da loja.
def obter_vendedores(self) -> list:
    return self.vendedor

#Retorna a lista de objetos Cliente da loja.
def obter_clientes(self) -> list:
    return self.cliente

#Retorna a lista de objetos Item.
def obter_items(self) -> list:
    return self.item

#Cria um novo objeto Gestor, que passa a ser o gestor da loja.
def registar_gestor(self, nome : str, numero_de_funcionario : str) -> None:
    self.gestor = Gestor(nome,numero_de_funcionario)
    
#Cria um novo objeto Vendedor, e regista-o na lista.
def registar_vendedor(self, nome : str, numero_de_funcionario : str) -> None:
    self.vendedor.append((Vendedor(nome,numero_de_funcionario))
  
#Cria um novo objeto Cliente, e regista-o na lista.
def registar_cliente(self, nome:str, numero_de_cliente:str) -> None:
    self.cliente.append(Cliente(nome,numero_de_cliente))
 
#Cria um novo objeto Item, e regista-o na lista.
def registar_item(self, nome : str) -> None:
    self.item.append((Item(nome))
                       
    
#Cria um novo objeto Fatura, com os objetos Cliente e Vendedor relativos aos números indicados, com um objeto Data com os parâmetros indicados, e regista-o na lista.
def registar_fatura(numero_de_cliente : str, itens : list, numero_de_funcionario_do_vendedor : str, ano : int, mes : int, dia : int) -> None:
    vendedor= None
    cliente= None
    
    for e in range (len(self.clientes)):
        if self.clientes[e].obter_numero() == numero_de_cliente:
            cliente = self.clientes[e]
        
    for e in range (len(self.vendedores)):
        if self.vendedores[e].numero == numero_de_funcionario_do_vendedor:
            vendedor = self.vendedores[e]
    
    cliente.faturas.append(fatura)
    vendedor.faturas.append(fatura)      
    
    
#Retorna a lista de objetos Fatura do cliente com o número indicado.
def obter_faturas_cliente( self numero_de_cliente : str) -> list:
    for e in range(len(self.clientes)):
        if self.clientes[e].obter_numero() == numero_de_cliente:
            return self.clientes[e].obter_faturas()
    
#Retorna a lista de objetos Fatura associados ao vendedor o número indicado
def obter_faturas_vendedor(self,numero_de_funcionario : str) -> list:
    for e in range(len(self.vendedores)):
        if self.vendedores[e].obter_numero() == numero_de_funcionario:
            return self.vendedores[e]
