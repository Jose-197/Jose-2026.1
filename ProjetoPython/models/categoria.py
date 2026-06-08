import json
from models.dao import DAO

class Categoria:
    def __init__(self, id, descricao):
        self.set_id(id)
        self.set_descricao(descricao)

    def __str__(self):
        return f"{self.__id} - {self.__descricao}"
    
    def get_id(self): return self.__id 

    def get_descricao(self): return self.__descricao

    def set_id(self, id):
        if id < 0: raise ValueError("Id não pode ser negativo")
        self.__id = id

    def set_descricao(self, descricao):
        if descricao == "": raise ValueError("Descrição não pode ser vazia")
        self.__descricao = descricao   

    def to_json(self):
        dic = {}
        dic["id"] = self.__id
        dic["descricao"] = self.__descricao
        return dic

    @staticmethod
    def from_json(dic):
        return Categoria(dic["id"], dic["descricao"])

class CategoriaDAO(DAO):
    def __init__(self):
        super().__init__(Categoria, "categorias.json")


class CategoriaDAO2:
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
        with open("categorias.json", mode="w") as arquivo:
            json.dump(self.objetos, arquivo, default = Categoria.to_json, indent=4)

    def abrir(self):
        self.objetos = []
        try:
            with open("categorias.json", mode="r") as arquivo:
                list_dic = json.load(arquivo)
                for dic in list_dic:
                    c = Categoria.from_json(dic)
                    self.objetos.append(c)
        except FileNotFoundError:
            self.objetos = []
