import cliente as cl
import produtos as pd

rodandoAdm = True

print("\nSeja bem-vindo ao Mercadinho Crocodile,\n")
print("Escolha uma opção:")
print("1. Administrador")
print("2. Cliente")

opcao = input("Opção (1/2): ")

if opcao == '1':
    senha = input("Digite a senha de administrador: ")
    if senha == '1234':

        print("\n--------------------------------")
        print("Bem-vindo, administrador!")
        while rodandoAdm:
            
            print("\nEscolha uma opção:")
            print("1. Ver Categorias")
            print("2. Ver Todos os Produtos")
            print("3. Adicionar Produto")
            print("4. Editar Produto")
            print("5. Excluir Produto")
            print("6. Sair")

            opc = input("Opção (1/2/3/4/5/6): ")

            if opc == '1':
                print("\n--------------------------------")
                print("Categorias Cadastradas:")
                for i, ct in enumerate(pd.categorias, 1):
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
                for categoria, produtos_categoria in pd.prod_categoria.items():
                    print(f"\n{categoria}:")
                    for produto in produtos_categoria:
                        preco = pd.preco_prod[produto]
                        quantidade = pd.quantidade_prod[produto]
                        print(f"- {produto} (R${preco:.2f}) - Quantidade: {quantidade}")
                    print("--------------------------------")

                print("Próximo! Escolha uma opção:")
                print("1. Ver Categoria Específica")
                print("2. Voltar")
                print("3. Sair")

                prox2 = input("Opção (1/2/3): ")

                if prox2 == '1':                 
                    categoria_escolhida = input("\nDigite o número (1 a 7) ou o nome da categoria: ")
                    if categoria_escolhida.isdigit():
                        categoria_escolhida = int(categoria_escolhida)
                        if categoria_escolhida >= 1 and categoria_escolhida <= len(pd.categorias):
                            categoria_escolhida = pd.categorias[categoria_escolhida - 1]
                        else:
                            print("Número de categoria inválido.")
                            continue

                    if categoria_escolhida in pd.categorias:
                        print("\n--------------------------------")
                        print(f"Produtos na categoria '{categoria_escolhida}':")
                        for produto in pd.prod_categoria[categoria_escolhida]:
                            preco = pd.preco_prod[produto]
                            quantidade = pd.quantidade_prod[produto]
                            print(f"- {produto} (R${preco:.2f}) - Quantidade: {quantidade}")
                        print("--------------------------------")
                    else:
                        print("Categoria não encontrada.")

                elif prox2 == '2':
                    continue

                elif prox2 == '3':
                    break

                else:
                    print("Opção inválida. Tente novamente.")

            elif opc == '3':

                print("\n--------------------------------")
                print("Categorias Cadastradas:")
                for i, ct in enumerate(pd.categorias, 1):
                    print(f"{i}. {ct}")
                print("--------------------------------")

                nome_produto = input("\nDigite o nome do novo produto: ")
                categoria_produto = input("Digite o número ou o nome da categoria do novo produto: ")
                if categoria_produto.isdigit():
                    categoria_produto = int(categoria_produto)
                    if categoria_produto >= 1 and categoria_produto <= len(pd.categorias):
                        categoria_produto = pd.categorias[categoria_produto - 1]
                    else:
                        print("Número de categoria inválido.")
                        continue

                categoria_encontrada = categoria_produto.capitalize()

                if categoria_encontrada:

                    preco_produto = float(input(f"Digite o preço de {nome_produto}: "))
                    quantidade_produto = int(input(f"Digite a quantidade de {nome_produto}: "))

                    novo_produto = f"{nome_produto} ({quantidade_produto})"
                    pd.prod_categoria[categoria_encontrada].append(novo_produto)
                    pd.preco_prod[novo_produto] = preco_produto
                    pd.quantidade_prod[novo_produto] = quantidade_produto

                    print(f"{novo_produto} foi adicionado à categoria {categoria_encontrada.capitalize()} com sucesso!")
                    print("--------------------------------")

                else:
                    print("Categoria não encontrada.")

            elif opc == '4':
                print("\nProdutos Cadastrados:")

                for categoria, produtos_categoria in pd.prod_categoria.items():
                    print(f"\n{categoria}:")
                    for i, produto in enumerate(produtos_categoria, 1):
                        print(f"{i}. {produto}")
                    print("--------------------------------")

                categoria_editar = input("Digite o número(1 a 7) ou o nome da categoria para editar um produto: ")
                if categoria_editar.isdigit():
                    categoria_editar = int(categoria_editar)
                    if categoria_editar >= 1 and categoria_editar <= len(pd.categorias):
                        categoria_editar = pd.categorias[categoria_editar - 1]
                    else:
                        print("Número de categoria inválido.")
                        continue

                categoria_editar = categoria_editar.capitalize()

                if categoria_editar in pd.prod_categoria:
                    print(f"\nProdutos na categoria '{categoria_editar}':")
                    for i, produto in enumerate(pd.prod_categoria[categoria_editar], 1):
                        print(f"{i}. {produto}")
                    numero_produto_editar = int(input("Digite o número correspondente ao produto que deseja editar: "))

                    if numero_produto_editar >= 1 and numero_produto_editar <= len(pd.prod_categoria[categoria_editar]):
                        produto_editar = pd.prod_categoria[categoria_editar][numero_produto_editar - 1]

                        nome_produto_editar = input("Digite o novo nome para o produto: ")
                        preco_produto_editar = float(input("Digite o novo preço para o produto: "))
                        quantidade_produto_editar = int(input("Digite a nova quantidade para o produto: "))

                        novo_produto_editar = f"{nome_produto_editar} ({quantidade_produto_editar})"
                        pd.prod_categoria[categoria_editar][numero_produto_editar - 1] = novo_produto_editar
                        pd.preco_prod.pop(produto_editar)
                        pd.quantidade_prod.pop(produto_editar)

                        pd.preco_prod[novo_produto_editar] = preco_produto_editar
                        pd.quantidade_prod[novo_produto_editar] = quantidade_produto_editar

                        print(f"Produto editado com sucesso para: {novo_produto_editar}")
                    else:
                        print("Número de produto inválido.")

                else:
                    print("Categoria não encontrada.")

            elif opc == '5':
                print("\nProdutos Cadastrados:")

                for categoria, produtos_categoria in pd.prod_categoria.items():
                    print(f"\n{categoria}:")
                    for i, produto in enumerate(produtos_categoria, 1):
                        print(f"{i}. {produto}")
                    print("--------------------------------")

                categoria_excluir = input("Digite o número(1 a 7) ou o nome da categoria para excluir um produto: ")
                if categoria_excluir.isdigit():
                    categoria_excluir = int(categoria_excluir)
                    if categoria_excluir >= 1 and categoria_excluir <= len(pd.categorias):
                        categoria_excluir = pd.categorias[categoria_excluir - 1]
                    else:
                        print("Número de categoria inválido.")
                        continue

                categoria_excluir = categoria_excluir.capitalize()

                if categoria_excluir in pd.prod_categoria:
                    print(f"\nProdutos na categoria '{categoria_excluir}':")
                    for i, produto in enumerate(pd.prod_categoria[categoria_excluir], 1):
                        print(f"{i}. {produto}")
                    numero_produto_excluir = int(input("Digite o número correspondente ao produto que deseja excluir: "))

                    if numero_produto_excluir >= 1 and numero_produto_excluir <= len(pd.prod_categoria[categoria_excluir]):
                        produto_excluir = pd.prod_categoria[categoria_excluir][numero_produto_excluir - 1]
                        pd.prod_categoria[categoria_excluir].pop(numero_produto_excluir - 1)
                        preco_excluido = pd.preco_prod.pop(produto_excluir, None)
                        quantidade_excluida = pd.quantidade_prod.pop(produto_excluir, None)

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