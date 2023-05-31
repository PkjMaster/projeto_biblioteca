from time import strptime
import os

linha = "\n"+"-"*30+"\n\n"  # linha pra fazer a formatação bonitinha

def limpar():#Função pra limpar o terminal e deixar bonitinho
    os.system("cls")

def lista_livro():
    # função pra colocar os dados dos arquivos em listas com o seguinte formato:

    #                       Livro1                              Livro2
    # lista=[[codigo,titulo,autor,ano,exemplares],[codigo,titulo,autor,ano,exemplares],[...]]

    lista_separada = []
    with open("livros.txt", "r", encoding="utf8") as arquivo:
        lista = arquivo.readlines()
    for linha in lista:
        linha.strip("\n")
        lista_separada.append(linha.split("|"))
        return lista_separada


def lista_usuario():
    # função pra colocar os dados dos arquivos em listas com o seguinte formato:

    #         Usuario1      Usuario2
    # lista=[[codigo,nome],[codigo,nome],[...]]

    lista_separada = []
    with open("usuarios.txt", "r", encoding="utf8") as arquivo:
        lista = arquivo.readlines()
    for linha in lista:
        linha.strip("\n")
        lista_separada.append(linha.split("|"))
        return lista_separada


def lista_reserva():
    # função pra colocar os dados dos arquivos em listas com o seguinte formato:

    #                    Reserva1                             Reserva2
    # lista=[[codigo,usuario,livro,data,status],[codigo,usuario,livro,data,status],[...]]

    lista_separada = []
    with open("reservas.txt", "r", encoding="utf8") as arquivo:
        lista = arquivo.readlines()
    for linha in lista:
        linha.strip("\n")
        lista_separada.append(linha.split("|"))
        return lista_separada


def cadastro_livro():
    livros = lista_livro()
    codigo = len(livros)-1
    while True:
        codigo += 1
        if livros[-1][0] != codigo and livros[-1][0] < codigo:
            limpar()
            titulo = input(linha, "Coloque o titulo do livro: ").strip(" ")
            limpar()
            autor = input(linha, "Coloque o nome do autor: ").strip(" ")
            limpar()
            ano_publicacao = input(
                linha, "Coloque o ano que o livro foi publicado ").strip(" ")
            while ano_publicacao.isnumeric() == False and len(ano_publicacao) != 4:
                limpar()
                print(linha, "Valor invalido!\nUse o seguinte modelo: YYYY\n")
                ano_publicacao = input(
                    "Coloque o ano que o livro foi publicado: ").strip(" ")
            limpar()
            quantidade_exemplares = input(
                linha, "Coloque a quantidade de exemplares do livro: ").strip(" ")
            while quantidade_exemplares.isnumeric() == False:
                limpar()
                print(linha, "Valor invalido!\n")
                quantidade_exemplares = input(
                    "Coloque a quantidade de exemplares do livro: ").strip(" ")
            with open("livros.txt", "a", encoding="utf8") as arquivo:
                arquivo.write(
                    f"{codigo}|{titulo}|{autor}|{ano_publicacao}|{quantidade_exemplares}\n")
            limpar()
            resposta = input(
                linha, "Deseja cadastrar mais um livro(sim ou não)? ").lower()
            if resposta.strip(" ")[0] == "n":
                limpar()
                input(
                    linha, "Operação Finalizada!\n(aperte enter para voltar ao menu)")
                return
            elif resposta.strip(" ")[0] != "s":
                limpar()
                input(linha, "\n\nOpção invalida!\n(aperte enter para voltar ao menu)")
                return


def cadastro_usuario():
    usuarios = lista_usuario()
    codigo = len(usuarios)-1
    while True:
        codigo += 1
        if usuarios[-1][0] != codigo and usuarios[-1][0] < codigo:
            limpar()
            nome = input(linha, "\nColoque o nome do usuario: ").strip(" ")
            limpar()
            email = input(linha, "\nColoque o email do usuario: ").strip(" ")
            limpar()
            telefone=input(linha, "\nColoque o telefone do usuario: ").strip(" ")
            with open("usuarios.txt", "a", encoding="utf8") as arquivo:
                arquivo.write(f"{codigo}|{nome}|{email}|{telefone}\n")
            limpar()
            resposta = input(
                linha, "\nDeseja cadastrar mais um usuario(sim ou não)? ").lower()
            if resposta.strip(" ")[0] == "n":
                limpar()
                input(
                    linha, "Operação Finalizada!\n(aperte enter para voltar ao menu)")
                return
            elif resposta.strip(" ")[0] != "s":
                limpar()
                input(linha, "Opção invalida!\n(aperte enter para voltar ao menu)")
                return


def reserva_livro():
    livros = lista_livro()
    usuarios = lista_usuario()
    reservas = lista_reserva()
    codigo = len(reservas)-1
    codigos_cadastrados_usuarios = []
    codigos_cadastrados_livros = []
    livros_atualizados = []
    while True:
        codigo += 1
        # verifica se ja existe algum codigo identico
        if reservas[-1][0] != codigo and reservas[-1][0] < codigo or reservas[-1][0].isnumeric() == False:
            print(linha, end="")
            for usuario in usuarios[1:-1]:
                # Imprime o codigo e o nome dos usuarios cadastrados sendo: usuario[0]=codigo e usuario[1]=nome
                print(f"[{usuario[0]}] - {usuario[1]}")
                codigos_cadastrados_usuarios.append(usuario[0])
            codigo_usuario = input(
                linha, "Digite o codigo do usuario que deseja fazer a reserva: ").strip(" ")
            # Verifica se o codigo digitado existe no sistema
            while codigo_usuario not in codigos_cadastrados_usuarios:
                print(linha, "O codigo digitado não está cadastrado!\n")
                codigo_usuario = input(
                    "Digite o codigo do usuario que deseja fazer a reserva: ").strip(" ")
            
            limpar()
            for livro in livros[1:]:
                # Imprime o codigo e o nome dos livros cadastrados sendo: livro[0]=codigo, livro[1]=Titulo livro[4]=Exemplares
                print(f"[{livro[0]}] - {livro[1]} | Exemplares: {livro[4]}")

                if int(livro[4]) > 0:  # Verifica se existe algum exemplar
                    codigos_cadastrados_livros.append(livro[0])

            codigo_livro = input(
                linha, "Digite o codigo do livro que deseja fazer a reserva: ").strip(" ")
            # Verifica se o codigo está cadastrado e se possui exemplares
            while codigo_livro not in codigos_cadastrados_livros:
                print(
                    linha, "O codigo do livro não está cadastrado ou não possui exemplares disponiveis!\n")
                codigo_livro = input(
                    "Digite o codigo do livro que deseja fazer a reserva: ").strip(" ")
            limpar()
            data = input(
                linha, "Usando o seguinte modelo (01/01/2000)\nColoque a data que a reserva foi publicado: ").strip(" ")
            while True:
                try:  # Verifica se a data inserida é valida para manipulação no futuro
                    strptime(data, "%d/%m/%Y")
                    break
                except ValueError:
                    limpar()
                    print(linha, "Valor invalido!\nUse o seguinte modelo: 01/01/2000\n")
                    data = input(
                        "Coloque o ano que o livro foi publicado: ").strip(" ")

            for livro in livros:
                if livro[0] == codigo_livro:  # Diminui o valor do quantidade exemplares do livro
                    livro[4] -= 1
                # Adiciona as strings formatadas em uma lista
                livros_atualizados.append("|".join(livro)+"\n")

            with open("livros.txt", "w", encoding="utf8") as arquivo:
                # Atualiza o valor de exemplares do livro
                arquivo.writelines(livros_atualizados)

            with open("reservas.txt", "a", encoding="utf8") as arquivo:  # Guarda os dados da reserva
                arquivo.write(
                    f"{codigo}|{codigo_usuario}|{codigo_livro}|{data}|Ativa\n")

def criador_menu(dicionario,texto):# Serve para criar o menu por meio de um dicionario   
    while True:
        limpar()
        print(f'''-----------------------------------
        {texto}
-----------------------------------''')
        for numero,item in dicionario.items():
            print(f"[{numero}]-{item}")
        opt=input("\n>").strip(" ")
        if opt in dicionario.keys():
            return opt
        else:
            limpar()
            input("""-----------------------------------
        Valor Invalido!
-----------------------------------
    Pressione Enter para continuar
-----------------------------------
""")
    
def menu_pesquisar():
    # Esses dicionarios são utilizados para criar o menu para cada uma das opções
    livros={"1":"Codigo","2":"Título","3":"Autor","4":"Ano"}
    usuarios={"1":"Codigo","2":"Nome"}
    reservas={"1":"Codigo","2":"Título","3":"Código do Livro","4":"Código do Usuário"}
    texto_menu="Como deseja pesquisar?"
    limpar()
    opt=input(f'''-----------------------------------
    Menu Pesquisar
-----------------------------------
[1]-Livros
[2]-Usuários
[3]-Reservas

>''').strip(" ")
    if opt == "1":
        criador_menu(livros,texto_menu)
    elif opt=="2":
        criador_menu(usuarios,texto_menu)
    elif opt=="3":
        criador_menu(reservas,texto_menu)
menu_pesquisar()