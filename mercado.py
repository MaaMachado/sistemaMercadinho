import cliente as cl

categorias = ["Congelados", "Higiene Pessoal", "Limpeza", "Alimentos embalados", "Molhos", "Bebidas", "Hortifruti"]
prod_categoria = {
    "Congelados": ["Pizza", "Filé de Peixe", "Peito de Frango"],
    "Higiene Pessoal": ["Creme Dental", "Papel Higiênico", "Sabonete"],
    "Limpeza": ["Sabão em pó", "Detergente", "Água sanitária"],
    "Alimentos embalados": ["Feijão", "Arroz", "Macarrão"],
    "Molhos": ["Ketchup", "Maionese", "Creme de Leite"],
    "Bebidas": ["Coca-cola", "Água Mineral", "Vodka Skyy", "Red Label"],
    "Hortifruti": ["Maçã", "Batata Inglesa", "Alface", "Cebola"]
}

preco_prod = {
    "Pizza": 14.99,
    "Filé de Peixe": 16.98,
    "Peito de Frango": 9.68,
    "Creme Dental": 3.29,
    "Papel Higiênico": 17.45,
    "Sabonete": 2.19,
    "Sabão em pó": 14.99,
    "Detergente": 3.40,
    "Água sanitária": 4.40,
    "Feijão": 7.29,
    "Arroz": 5.59,
    "Macarrão": 3.49,
    "Ketchup": 7.77,
    "Maionese": 8.99,
    "Creme de Leite": 2.89,
    "Coca-cola": 6.49,
    "Água Mineral": 2.39,
    "Vodka Skyy": 35.14,
    "Red Label": 42.90,
    "Maçã": 12.90,
    "Batata Inglesa": 5.80,
    "Alface": 6.99,
    "Cebola": 2.39
}

quantidade_prod = {
    "Pizza": 12,
    "Filé de Peixe": 6,
    "Peito de Frango": 8,
    "Creme Dental": 20,
    "Papel Higiênico": 20,
    "Sabonete": 20,
    "Sabão em pó": 15,
    "Detergente": 20,
    "Água sanitária": 15,
    "Feijão": 20,
    "Arroz": 20,
    "Macarrão": 20,
    "Ketchup": 18,
    "Maionese": 18,
    "Creme de Leite": 18,
    "Coca-cola": 15,
    "Água Mineral": 30,
    "Vodka Skyy": 10,
    "Red Label": 6,
    "Maçã": 30,
    "Batata Inglesa": 35,
    "Alface": 16,
    "Cebola": 25
}

rodandoAdm = True

print("\nSeja bem-vindo ao Mercadinho Crocodile,\n")
print("Escolha uma opção:")
print("1. Administrador")
print("2. Cliente")

opcao = input("Opção (1/2): ")

if opcao == '1':
    senha = input("Digite a senha de administrador: ")
    if senha == '1234':

        while rodandoAdm:
            print("\nBem-vindo, administrador!\n")
            print("Escolha uma opção:")
            print("1. Ver Categorias")
            print("2. Ver Todos os Produtos")
            print("3. Adicionar Produto")
            print("4. Editar Produto")
            print("5. Excluir Produto")
            print("6. Sair")

            opc = input("Opção (1/2/3/4/5/6): ")

            if opc == '1':
                print("\nCategorias Cadastradas:")
                for i, ct in enumerate(categorias, 1):
                    print(f"{i}. {ct}")
                print("--------------------------------")

                print("Próximo! Escolha uma opção:")
                print("1. Voltar")
                print("2. Sair")

                prox = input("Opção (1/2): ")

                if prox == '1':
                    continue
                elif prox == '2':
                    break
                else:
                    print("Opção inválida. Tente novamente.")

            elif opc == '2':
                print("\nProdutos Cadastrados:")

                for categoria, produtos_categoria in prod_categoria.items():
                    print(f"\n{categoria}:")
                    for produto in produtos_categoria:
                        preco = preco_prod[produto]
                        quantidade = quantidade_prod[produto]
                        print(f"- {produto} (R${preco:.2f}) - Quantidade: {quantidade}")
                    print("--------------------------------")

                print("Próximo! Escolha uma opção:")
                print("1. Ver Categoria Específica")
                print("2. Voltar")
                print("3. Sair")

                prox2 = input("Opção (1/2/3): ")

                if prox2 == '1':
                    categoria_escolhida = input("Digite o número ou o nome da categoria: ")
                    if categoria_escolhida.isdigit():
                        categoria_escolhida = int(categoria_escolhida)
                        if categoria_escolhida >= 1 and categoria_escolhida <= len(categorias):
                            categoria_escolhida = categorias[categoria_escolhida - 1]
                        else:
                            print("Número de categoria inválido.")
                            continue
                    categoria_escolhida = categoria_escolhida.capitalize()

                    if categoria_escolhida in prod_categoria.keys():
                        print(f"\nProdutos na categoria '{categoria_escolhida}':")
                        for produto in prod_categoria[categoria_escolhida]:
                            preco = preco_prod[produto]
                            quantidade = quantidade_prod[produto]
                            print(f"- {produto} (R${preco:.2f}) - Quantidade: {quantidade}")
                    else:
                        print("Categoria não encontrada.")

                elif prox2 == '2':
                    continue

                elif prox2 == '3':
                    break

                else:
                    print("Opção inválida. Tente novamente.")

            elif opc == '3':

                print("\nCategorias Cadastradas:")
                for i, ct in enumerate(categorias, 1):
                    print(f"{i}. {ct}")

                nome_produto = input("\nDigite o nome do novo produto: ")
                categoria_produto = input("Digite o número ou o nome da categoria do novo produto: ")
                if categoria_produto.isdigit():
                    categoria_produto = int(categoria_produto)
                    if categoria_produto >= 1 and categoria_produto <= len(categorias):
                        categoria_produto = categorias[categoria_produto - 1]
                    else:
                        print("Número de categoria inválido.")
                        continue

                categoria_encontrada = categoria_produto.capitalize()

                if categoria_encontrada:

                    preco_produto = float(input(f"Digite o preço de {nome_produto}: "))
                    quantidade_produto = int(input(f"Digite a quantidade de {nome_produto}: "))

                    novo_produto = f"{nome_produto} ({quantidade_produto})"
                    prod_categoria[categoria_encontrada].append(novo_produto)
                    preco_prod[novo_produto] = preco_produto
                    quantidade_prod[novo_produto] = quantidade_produto

                    print(f"{novo_produto} foi adicionado à categoria {categoria_encontrada.capitalize()} com sucesso!")
                    print("--------------------------------")

                else:
                    print("Categoria não encontrada.")

            elif opc == '4':
                print("\nProdutos Cadastrados:")

                for categoria, produtos_categoria in prod_categoria.items():
                    print(f"\n{categoria}:")
                    for i, produto in enumerate(produtos_categoria, 1):
                        print(f"{i}. {produto}")
                    print("--------------------------------")

                categoria_editar = input("Digite o número ou o nome da categoria para editar um produto: ")
                if categoria_editar.isdigit():
                    categoria_editar = int(categoria_editar)
                    if categoria_editar >= 1 and categoria_editar <= len(categorias):
                        categoria_editar = categorias[categoria_editar - 1]
                    else:
                        print("Número de categoria inválido.")
                        continue

                categoria_editar = categoria_editar.capitalize()

                if categoria_editar in prod_categoria:
                    print(f"\nProdutos na categoria '{categoria_editar}':")
                    for i, produto in enumerate(prod_categoria[categoria_editar], 1):
                        print(f"{i}. {produto}")
                    numero_produto_editar = int(input("Digite o número correspondente ao produto que deseja editar: "))

                    if numero_produto_editar >= 1 and numero_produto_editar <= len(prod_categoria[categoria_editar]):
                        produto_editar = prod_categoria[categoria_editar][numero_produto_editar - 1]

                        nome_produto_editar = input("Digite o novo nome para o produto: ")
                        preco_produto_editar = float(input("Digite o novo preço para o produto: "))
                        quantidade_produto_editar = int(input("Digite a nova quantidade para o produto: "))

                        novo_produto_editar = f"{nome_produto_editar} ({quantidade_produto_editar})"
                        prod_categoria[categoria_editar][numero_produto_editar - 1] = novo_produto_editar
                        preco_prod.pop(produto_editar)
                        quantidade_prod.pop(produto_editar)

                        preco_prod[novo_produto_editar] = preco_produto_editar
                        quantidade_prod[novo_produto_editar] = quantidade_produto_editar

                        print(f"Produto editado com sucesso para: {novo_produto_editar}")
                    else:
                        print("Número de produto inválido.")

                else:
                    print("Categoria não encontrada.")

            elif opc == '5':
                print("\nProdutos Cadastrados:")

                for categoria, produtos_categoria in prod_categoria.items():
                    print(f"\n{categoria}:")
                    for i, produto in enumerate(produtos_categoria, 1):
                        print(f"{i}. {produto}")
                    print("--------------------------------")

                categoria_excluir = input("Digite o número ou o nome da categoria para excluir um produto: ")
                if categoria_excluir.isdigit():
                    categoria_excluir = int(categoria_excluir)
                    if categoria_excluir >= 1 and categoria_excluir <= len(categorias):
                        categoria_excluir = categorias[categoria_excluir - 1]
                    else:
                        print("Número de categoria inválido.")
                        continue

                categoria_excluir = categoria_excluir.capitalize()

                if categoria_excluir in prod_categoria:
                    print(f"\nProdutos na categoria '{categoria_excluir}':")
                    for i, produto in enumerate(prod_categoria[categoria_excluir], 1):
                        print(f"{i}. {produto}")
                    numero_produto_excluir = int(input("Digite o número correspondente ao produto que deseja excluir: "))

                    if numero_produto_excluir >= 1 and numero_produto_excluir <= len(prod_categoria[categoria_excluir]):
                        produto_excluir = prod_categoria[categoria_excluir][numero_produto_excluir - 1]
                        prod_categoria[categoria_excluir].pop(numero_produto_excluir - 1)
                        preco_excluido = preco_prod.pop(produto_excluir, None)
                        quantidade_excluida = quantidade_prod.pop(produto_excluir, None)

                        if preco_excluido is not None and quantidade_excluida is not None:
                            print(f"Produto excluído com sucesso: {produto_excluir}")
                        else:
                            print("Erro ao excluir o produto.")
                    else:
                        print("Número de produto inválido.")

                else:
                    print("Categoria não encontrada.")

            elif opc == '6':
                break

            else:
                print("Opção inválida. Tente novamente.")

    else:
        print("Senha incorreta. Acesso negado.")

elif opcao == '2':
    cl.inform()

else:
    print("Opção inválida. Tente novamente.")