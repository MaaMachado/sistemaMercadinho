def inform():
    
    import produtos as pd
    rodandoCliente = True
    rodVenda = True

    print("------------------------------------------------------------------")
    print("Bem-vindo ao Mercadinho Mais Charmoso da sua Cidade, cliente!\n")
    print("Primeiramente, necessitamos de algumas informações para dar continuidade ao nosso atendimento online.\n")

    while rodandoCliente:
        print("O senhor(a) reside na cidade de Salvador? ")
        cidade = input("Opção (s/n): ")

        if cidade == "s":
            print("\nÓtimo! Agora, O senhor(a) reside no bairro de Brotas? ")
            bairro = input("Opção (s/n): ")
            if bairro == "s":
                print("\nMaravilhoso!\nJá sabendo que o senhor(a) está dentro da localidade do Mercadinho Crocodile. Vamos dar continuidade no nosso atendiemnto.")
                print("\nCADASTRO DE CLIENTE:")
                nome = input ("Digite o seu nome: ")
                idade = input ("Digite a sua idade: ")

                if idade <= '12':
                    print("\nPeço desculpas, mas a idade não foi autorizada. Esperamos que, no futuro, possa comprar com a gente novamente.\n")
                    break

                elif idade > '12' and idade <= '90':

                    print("\nENDEREÇO:")
                    rua = input ("Digite o nome da sua rua(Ex: 'Rua..' ou 'Avenida..'): ")
                    if rua[:3] == "Rua" or rua[:3] == "rua" or rua[:7] == "Avenida" or rua[:7] == "avenida":
                        try:
                            numEnd = int(input ("Digite o número: "))
                        except ValueError as e:
                            print("\n-------------------")
                            print(f"Error: {e}")
                            print("Digite um número!")
                            print("-------------------")
                            print("Reiniciando questionário...")
                            print("--------------------------------\n")
                            continue

                        print("-----------------------------------")
                        print(f"\nConfirme suas informações: \nNome: {nome} - Idade: {idade} anos - Endereço: {rua}, {numEnd}.")
                        infoCliente = input("Está certo(s/n)? ")
                        if infoCliente == "s":
                            print("\nPerfeito! Agora vamos prosseguir para etapa da venda.")

                            carrinho = {}
                            idade_cliente = int(idade)

                            while rodVenda:
                                print("\nMENU DE VENDA:")
                                print("1. Escolher Produto")
                                print("2. Ver Carrinho")
                                print("3. Sair")

                                opcao_venda = input("Escolha uma opção (1/2/3): ")

                                if opcao_venda == "1":
                                    print("\nPrimeiramente, escolha uma categoria para que todos os seus produtos sejam listados para sua escolha.")
                                    print("---------------------------------------------------------------------------------------------------------")

                                    print("Categorias Disponíveis:")
                                    for i, categoria in enumerate(pd.categorias, 1):
                                        print(f"{i}. {categoria}")
                                    print("------------------------------")

                                    categoria_escolhida = input("Escolha a categoria (1 a 7): ")
                                    if categoria_escolhida.isdigit():
                                        categoria_escolhida = int(categoria_escolhida)
                                        if 1 <= categoria_escolhida <= len(pd.categorias):
                                            categoria_escolhida = pd.categorias[categoria_escolhida - 1]
                                        else:
                                            print("Número de categoria inválido.")
                                            continue
                                    
                                    categoria_escolhida = categoria_escolhida.capitalize()

                                    if categoria_escolhida in pd.categorias:
                                        print("\n---------------------------------------------------")
                                        print(f"Produtos na categoria '{categoria_escolhida}':")
                                        produtos_categoria = pd.prod_categoria[categoria_escolhida]
                                        for i, produto in enumerate(produtos_categoria, 1):
                                            preco = pd.preco_prod[produto]
                                            print(f"{i}. {produto} (R${preco:.2f})")

                                        escolha_produto = input("\nEscolha o número do produto que deseja comprar (ou digite 's' para voltar ao Menu): ")

                                        if escolha_produto == 's':
                                            continue

                                        if escolha_produto.isdigit():
                                            escolha_produto = int(escolha_produto)

                                            if 1 <= escolha_produto <= len(produtos_categoria):
                                                produto_selecionado = produtos_categoria[escolha_produto - 1]
                                                preco_produto = pd.preco_prod[produto_selecionado]

                                                
                                                if produto_selecionado in ("Vodka Skyy", "Red Label") and idade_cliente < 18:
                                                    print("Você não tem idade suficiente para comprar bebidas alcoólicas.")
                                                    continue

                                                quantidade_desejada = int(input("Digite a quantidade desejada: "))

                                                if quantidade_desejada <= pd.quantidade_prod[produto_selecionado]:
                                                    if produto_selecionado in carrinho:
                                                        carrinho[produto_selecionado]["quantidade"] += quantidade_desejada
                                                    else:
                                                        carrinho[produto_selecionado] = {
                                                            "preco": preco_produto,
                                                            "quantidade": quantidade_desejada
                                                        }
                                                    pd.quantidade_prod[produto_selecionado] -= quantidade_desejada
                                                    print(f"{quantidade_desejada} unidades de {produto_selecionado} foram adicionadas ao carrinho.")

                                                else:
                                                    print("Quantidade indisponível.")
                                                    continue

                                            else:
                                                print("Número de produto inválido.")
                                                continue

                                        else:
                                            print("Opção inválida. Tente novamente.")
                                            continue

                                    else:
                                        print("Categoria não encontrada.")
                                        continue

                                elif opcao_venda == "2":
                                    print("Teste")
                                    break

                                elif opcao_venda == "3":
                                    break

                                else:
                                    print("Opção inválida. Tente novamente.")
                                    continue 
                        
                        elif infoCliente == "n":
                            print("\nReiniciando questionário...")
                            print("--------------------------------")
                            continue
                        else:
                            print("Opção inválida. Tente novamente.")
                            continue
                    
                    else:
                        print("\n-------------------")
                        print("ERROR! Endereço inválido! Digite uma rua válida!")
                        print("-------------------")
                        print("Reiniciando questionário...")
                        print("--------------------------------\n")
                        continue
                
                else:
                    print("\nERRO! Dado digitado é inválido.")
                    print("-------------------------------")
                    print("Reiniciando questionário...")
                    print("--------------------------------\n")
                    continue


            elif bairro == "n":
                print("\nPeço desculpas, mas o Mercadinho Crocodile ainda não opera fora do bairro de Brotas. Esperamos que, no futuro, possamos ter uma filial em seu bairro.\n")
                break

            else:
                print("Opção inválida. Tente novamente.")
                continue

        elif cidade == "n":
            print("\nPeço desculpas, mas o Mercadinho Crocodile ainda não opera fora de Salvador. Esperamos que, no futuro, possamos ter uma filial em sua cidade.\n")
            break

        else:
            print("Opção inválida. Tente novamente.")
            continue


    else:
        print("Opção inválida. Tente novamente.")