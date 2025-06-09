produtos = []

def adicionar_produto():
    print("\n Adicionar Produto")
    nome = input("Nome do produto: ")
    preco = float(input("Preço: R$ "))
    quantidade = int(input("Quantidade: "))
    produto = {"nome": nome, "preco": preco, "quantidade": quantidade}
    produtos.append(produto)
    print(f"\n Produto '{nome}' adicionado com sucesso!\n")

def buscar_produto():
    print("\n Buscar Produto")
    nome = input("Digite o nome do produto: ")
    for produto in produtos:
        if produto["nome"].lower() == nome.lower():
            print("\n Produto encontrado:")
            print(f"Nome: {produto['nome']}")
            print(f"Preço: R$ {produto['preco']:.2f}")
            print(f"Quantidade: {produto['quantidade']}\n")
            return
    print("\n Produto não encontrado.\n")

def listar_produtos():
    print("\n Lista de Produtos")
    if not produtos:
        print("Nenhum produto cadastrado.\n")
        return
    for produto in produtos:
        print(f" {produto['nome']} | Preço: R$ {produto['preco']:.2f} | Quantidade: {produto['quantidade']}")
    print()

def atualizar_estoque():
    print("\n Atualizar Estoque")
    nome = input("Digite o nome do produto a atualizar: ")
    for produto in produtos:
        if produto["nome"].lower() == nome.lower():
            nova_quantidade = int(input("Nova quantidade: "))
            produto["quantidade"] = nova_quantidade
            print(f"\n Estoque de '{nome}' atualizado para {nova_quantidade} unidades.\n")
            return
    print("\n Produto não encontrado.\n")

def menu():
    while True:
        print("======= SISTEMA DE ESTOQUE =======")
        print("1. Adicionar produto")
        print("2. Buscar produto")
        print("3. Listar produtos")
        print("4. Atualizar estoque")
        print("5. Sair")
        escolha = input("Escolha uma opção (1-5): ")

        if escolha == "1":
            adicionar_produto()
        elif escolha == "2":
            buscar_produto()
        elif escolha == "3":
            listar_produtos()
        elif escolha == "4":
            atualizar_estoque()
        elif escolha == "5":
            print("\nEncerrando o sistema. Até logo!\n")
            break
        else:
            print("\n Opção inválida. Tente novamente.\n")

menu()
