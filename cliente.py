def inform():
    
    rodandoCliente = True

    print("------------------------------------------------------------------")
    print("Bem-vindo ao Mercadinho Mais Charmoso da sua Cidade, cliente!\n")
    print("Primeiramente, necessitamos de algumas informações para dar continuidade ao nosso atendimento online.\n")

    while rodandoCliente:
        print("O senhor(a) reside na cidade de Salvador? ")
        cidade = input("Opção (s/n): ")

        if cidade == "s":
            print("Ótimo! Agora, O senhor(a) reside no bairro de Brotas? ")
            bairro = input("Opção (s/n): ")
            if bairro == "s":
                print("Maravilhoso! Vamos dar continuidade no nosso atendiemnto.")
                print("\nCADASTRO DE CLIENTE:")
                nome = input ("Digite o seu nome: ")
                idade = input ("Digite a sua idade: ")
                print("Digite o seu endereço:")
                rua = input ("Digite o nome da sua rua: ")
                numEnd = int(input ("Digite o número: "))

                print("-----------------------------------")
                print(f"Confirme suas informações: \nNome: {nome} - Idades: {idade} - Endereço: {rua}, {numEnd}.")
                infoCliente = input("Está certo(s/n)? ")
                if infoCliente == "s":
                    print("Agora vamos prosseguir para etapa da venda.")
                
                elif infoCliente == "n":
                    print("Reiniciando questionário...")
                    continue
                else:
                    print("Opção inválida. Tente novamente.")
                    continue


            elif bairro == "n":
                print("Peço desculpas, mas o Mercadinho Crocodile ainda não opera fora do bairro de Brotas. Esperamos que, no futuro, possamos ter uma filial em seu bairro.")

            else:
                print("Opção inválida. Tente novamente.")
                continue

        elif cidade == "n":
            print("Peço desculpas, mas o Mercadinho Crocodile ainda não opera fora de Salvador. Esperamos que, no futuro, possamos ter uma filial em sua cidade.")
            break

        else:
            print("Opção inválida. Tente novamente.")
            continue


    else:
        print("Opção inválida. Tente novamente.")
