import json
from models.dao import DAO

class Cliente:
    def __init__(self, id, nome, email, fone, senha):
        self.set_id(id)          # atributo de instância
        self.set_nome(nome)      # cada cliente (instância) tem id e nome
        self.set_email(email)
        self.set_fone(fone)
        self.set_senha(senha)

    def __str__(self):
        return f"{self.__id} - {self.__nome} - {self.__email} - {self.__fone}"

    def get_id(self): return self.__id

    def get_nome(self): return self.__nome

    def get_email(self): return self.__email

    def get_fone(self): return self.__fone

    def get_senha(self): return self.__senha

    def set_id(self, id): self.__id = id

    def set_nome(self, nome): 
        if nome == "": raise ValueError("Nome não pode ser vazio")
        self.__nome = nome

    def set_email(self, email):
        if email == "": raise ValueError("E-mail não pode ser vazio")
        self.__email = email

    def set_fone(self, fone): 
        self.__fone = fone

    def set_senha(self, senha):
        if senha == "": raise ValueError("Senha não pode ser vazia")
        self.__senha = senha

    def to_json(self):
        return { "id" : self.__id, "nome" : self.__nome, "email" : self.__email, "fone" : self.__fone, "senha" : self.__senha }

    @staticmethod
    def from_json(dic):
        return Cliente(dic["id"], dic["nome"], dic["email"], dic["fone"], dic["senha"])

class ClienteDAO(DAO):
    def __init__(self):
        super().__init__(Cliente, "clientes.json")
    
    # Polimorfismo
    def listar(self):
        objetos = super().listar()
        objetos.sort(key = lambda x : x.get_nome().upper())
        return objetos

class ClienteDAO2:
    def __init__(self):
        self.objetos = []

    def inserir(self, obj):
        self.abrir()
        # auto-incremento do id - calcula o maior id usado e soma um
        if len(self.objetos) == 0: id = 1
        else: id = (max(self.objetos, key = lambda x : x.get_id())).get_id() + 1
        obj.set_id(id)
        self.objetos.append(obj)
        self.salvar()

    def listar(self):
        self.abrir()
        return self.objetos

    def listar_id(self, id):
        self.abrir()
        for obj in self.objetos:
            if obj.get_id() == id: return obj
        return None        

    def atualizar(self, obj):
        # x é objeto que já está na lista com os dados desatualiazados e tem o 
        # mesmo id do novo objeto - obj
        x = self.listar_id(obj.get_id())
        if x != None:
            self.objetos.remove(x)
            self.objetos.append(obj)
            self.salvar()

    def excluir(self, obj):
        x = self.listar_id(obj.get_id())
        if x != None:
            self.objetos.remove(x)
            self.salvar()

    def salvar(self):
        with open("clientes.json", mode="w") as arquivo:
            json.dump(self.objetos, arquivo, default = Cliente.to_json, indent=4)

    def abrir(self):
        self.objetos = []
        try:
            with open("clientes.json", mode="r") as arquivo:
                list_dic = json.load(arquivo)
                for dic in list_dic:
                    c = Cliente.from_json(dic)
                    self.objetos.append(c)
        except FileNotFoundError:
            self.objetos = []
            

