from operator import truediv

bibliotecas = {}
lixeira = []
while(True):

    print("\n===== MENU =====")
    print("1 - Adicionar biblioteca")
    print("2 - Adicionar pasta")
    print("3 - Adicionar fotos em uma pasta")
    print("4 - Ver bibliotecas")
    print("5 - Transferir para lixeira")
    print("6 - Ver lixeira")
    print("0 - Sair")

    menu = input("Escolha uma opção: ")

    match menu:
        case "1":
            # ==========================
            # ADICIONAR BIBLIOTECA
            # ==========================
            name_bibliotecas = input("Nome da biblioteca: ")

            if(name_bibliotecas in bibliotecas):
                print("Biblioteca já existe!")
            else:
                bibliotecas[name_bibliotecas] = {}
                print("Bibliotecas criada com sucesso!")

        case "2":
            # ==========================
            # ADICIONAR PASTA
            # ==========================
            name_bibliotecas = input("Nome da biblioteca: ")

            if(name_bibliotecas not in bibliotecas):
                print("biblioteca não encontrada")
            else:
                nome_pasta = input("Nome da pasta: ")

                if(nome_pasta  in bibliotecas[name_bibliotecas]):
                    print("Pasta já existe!")
                else:
                    bibliotecas[name_bibliotecas][nome_pasta] = []
                    print("Pasta criada com sucesso!")
        case "3":
            # ==========================
            # ADICIONAR FOTOS
            # ==========================
            name_bibliotecas = input("Digite a biblioteca: ")
            if(name_bibliotecas not in bibliotecas):
                print("Biblioteca não encontrada.")
            else:
                nome_pasta = input("Digite o nome da pasta: ")

                if(nome_pasta not in bibliotecas[name_bibliotecas]):
                    print("Pasta não encontrada.")
                else:
                    foto = input("Digite o nome da foto da pasta: ")
                    bibliotecas[name_bibliotecas][nome_pasta].append(foto)
        case "4":
            # ==========================
            # VER BIBLIOTECAS
            # ==========================
            if not bibliotecas:
                print("Nenhuma biblioteca cadastrada.")
            else:
                for biblioteca,pasta in bibliotecas.items():
                    print(f"\n📚 Bibliotecas: {biblioteca}")
                    for pasta,fotos in pasta.items():
                        print(f" 📁 Pasta: {pasta}")
                        if(fotos):
                            for foto in fotos:
                                print(f"  🖼️ {foto}")
                        else:
                            print(" Pasta vazia.")
        case "5":
            # ==========================
            # TRANSFERIR LIXEIRA
            # ==========================
            print("1 - Transferir biblioteca para lixeira")
            print("2 - Transferir pasta para lixeira")
            print("3 - Transferir foto para lixeira")
            print("0 - Sair")

            transf = input("Escolha uma opção: ")

            match transf:
                    case "1":
                        name_bibliotecas = input("Digite o nome da biblioteca: ")

                        if name_bibliotecas not in bibliotecas:
                            print("Biblioteca não encontrada.")
                        else:
                            resposta
                            while (True):
                                resposta=print("Certeza que deseja deletar? (sim ou não)")
                                if (resposta == "Sim" or "sim" or "Não" or "Nao" or "nao" or "não"):
                                    break

                            if(resposta == "Não" or "Nao" or "nao" or "não"):
                                break
                            else:

                                lixeira.append({
                                    "tipo": "pasta",
                                    "biblioteca": name_bibliotecas,
                                    "name": name_pasta,
                                    "conteudo": bibliotecas[name_bibliotecas]
                                })

                                del bibliotecas[name_bibliotecas]

                    case "2":
                        name_bibliotecas = input("Digite o nome da bibliotecas: ")

                        if name_bibliotecas not in bibliotecas:
                            print("Biblioteca não encontrada")
                        else:
                            name_pasta = input("Nome da pasta: ")

                            if(nome_pasta not in bibliotecas[name_bibliotecas]):
                                print("Pasta não encontrada.")
                            else:
                                lixeira.append({
                                    "tipo": "pasta",
                                    "biblioteca": name_bibliotecas,
                                    "name": name_pasta,
                                    "conteudo": bibliotecas[name_bibliotecas]
                                })

        case "6":
                # ==========================
                # VER LIXEIRA
                # ==========================

                if not lixeira:
                    print("Lixeira vazia.")

                else:

                    print("\n🗑️ Lixeira:")

                    for item in lixeira:
                        print(item)

        case "7":

                print("\n===== LIXEIRA =====")
                print("1 - Excluir biblioteca")
                print("2 - Excluir pasta")
                print("3 - Excluir fotos de uma pasta")
                print("0 - Sair")

                lixo = input("Escolha uma opção: ")

                match lixo:

                    case "1":
                    # ======================
                    # EXCLUIR BIBLIOTECA
                    # ======================
                        name_bibliotecas = input("Nome da biblioteca: ")

                        if (name_bibliotecas not in bibliotecas):
                            print("Biblioteca não existe!")
                        else:
                            del bibliotecas[name_bibliotecas]
                            print("Bibliotecas apagada com sucesso!")

                    case "2":
                    # ======================
                    # EXCLUIR PASTA
                    # ======================
                        name_bibliotecas = input("Nome da biblioteca: ")

                        if (name_bibliotecas not in bibliotecas):
                            print("biblioteca não encontrada")
                        else:
                            nome_pasta = input("Nome da pasta: ")

                            if (nome_pasta not in bibliotecas[name_bibliotecas]):
                                print("Pasta não existe!")
                            else:
                                del bibliotecas[name_bibliotecas][nome_pasta]
                                print("Pasta deletada com sucesso!")

                    case "3":
                    # ======================
                    # EXCLUIR FOTOS
                    # ======================
                        name_bibliotecas = input("Digite a biblioteca: ")

                        if (name_bibliotecas not in bibliotecas):
                            print("Biblioteca não encontrada.")
                        else:
                            nome_pasta = input("Digite o nome da pasta: ")

                            if (nome_pasta not in bibliotecas[name_bibliotecas]):
                                print("Pasta não encontrada.")
                            else:
                                foto = input("Digite o nome da foto da pasta: ")
                                bibliotecas[name_bibliotecas][nome_pasta].remove(foto)

                    case "0":
                        # ==========================
                        # SAIR
                        # ==========================
                            print("Fechando lixeira.")
                            break
                    case _:
                        print("Opção inválida.")


        case "0":
                # ==========================
                # SAIR
                # ==========================
                    print("Encerrando o sistema...")
                    break
        case _:
                print("Opção inválida.")

