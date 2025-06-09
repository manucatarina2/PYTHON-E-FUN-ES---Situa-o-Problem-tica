produtos = []
def adicionar_produto(nome, preco, quantidade):
    produto = {
        "nome": nome,
        "preco": preco,
        "quantidade": quantidade
    }
    produtos.append(produto)
    print(f"Produto '{nome}' adicionado com sucesso!")

def buscar_produto(nome):
    for produto in produtos:
        if produto["nome"].lower() == nome.lower():
            return produto
    return None

def atualizar_estoque(nome, nova_quantidade):
    produto = buscar_produto(nome)
    if produto:
        produto["quantidade"] = nova_quantidade
        print(f"Estoque de '{nome}' atualizado para {nova_quantidade} unidades.")
    else:
        print(f"Produto '{nome}' não encontrado.")

def listar_produtos():
    print("=== Lista de Produtos ===")
    for produto in produtos:
        print(f"{produto['nome']} | Preço: R${produto['preco']} | Quantidade: {produto['quantidade']}")
    print("=========================")

adicionar_produto("Arroz", 5.99, 30)
adicionar_produto("Feijão", 7.50, 20)

listar_produtos()

produto = buscar_produto("Arroz")
if produto:
    print(f"Produto encontrado: {produto}")
else:
    print("Produto não encontrado.")

atualizar_estoque("Feijão", 15)
listar_produtos()
