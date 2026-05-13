from unittest import case

bibliotecas = {}
lixeira= []
while(True):

    print("\n===== MENU =====")
    print("1 - Adicionar biblioteca")
    print("2 - Adicionar pasta")
    print("3 - Adicionar fotos em uma pasta")
    print("4 - Ver bibliotecas")
    print("5 - Ver lixeira")
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
                    foto = input("Digite o Nome da foto da pasta: ")
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
            # VER LIXEIRA
            # ==========================

            if not lixeira:
                print("Lixeira vazia.")

            else:

                print("\n🗑️ Lixeira:")

                for item in lixeira:
                    print(item)
        case "0":
            # ==========================
            # SAIR
            # ==========================
                print("Encerrando o sistema...")
                break
        case _:
            print("Opção inválida.")