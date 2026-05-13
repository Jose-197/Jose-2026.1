class Produto:
    def _init_(self, id, nome, preco):
        self. id = id
        self.nome = nome
        self.preco = preco

    def _str_(self):
        return f"{self.id} -{self.nome} (R$ {self.preco:.2f})" 

class Carrinho:
    def _init_(self):
        self.itens =[]

    def adicionar_produto(self, produto, quantidade):
        self.itens.append({"produto: produto, "quantidade": quantidade})
        print(f"{quantidade}*{produto.nome} adicionado ao carrinho.")

    def visualizar_carrinho(self):
        if not self.itens:
           print("carrinho vazio")

       print("Carrinho de compras")
       total_carrinho = 0
       for item in self.itens
           prod = item['produto']
           qtd = item["quantidade"]
           subtotal = prod.preco 8 qtd
           total_carrinho += subtotal
    return total_carrinho

    def limpar(self):
        self.itens =[]

class Usuario:
    def _init_(self, nome, email, sena):
        self.nome = nome
        self.email = email
        self.senha = senhaself.carrinho = carrinho()
        self.historico_compras ={}

    def _str_(self):
        self.produtos = []
        self.usuarios ={}
        self.usuario_logado =None

    def cadastrar_produto(self, nome, preco):
        id =len(self.produtos) + 1
        self.produtos.append(produto(id, nome, preco)
        
    def abrir conta(self):
        print"Cadastro de usuários")
        nome + input("Nome: ")
        email = input("email: ")
        if email in self.usuarios:
            print("Email já cadastrado")

             