from time import strptime
import os

linha_simples = '-'*45
linha_composta = "\n"+"-"*45+"\n\n"  # linha pra fazer a formatação bonitinha


def limpar():  # Função pra limpar o terminal e deixar bonitinho
    os.system("cls")


def lista_livro():
    # função pra colocar os dados dos arquivos em listas com o seguinte formato:

    #                       Livro1                              Livro2
    # lista=[[codigo,titulo,autor,ano,exemplares],[codigo,titulo,autor,ano,exemplares],[...]]

    lista_separada = []
    with open("livros.txt", "r", encoding="utf8") as arquivo:
        lista = arquivo.readlines()
    for linha in lista:
        linha = linha.strip("\n")
        lista_separada.append(linha.split("|"))
    lista_separada.pop(0)  # Remove o modelo visual
    return lista_separada


def lista_usuario():
    # função pra colocar os dados dos arquivos em listas com o seguinte formato:

    #         Usuario1      Usuario2
    # lista=[[codigo,nome],[codigo,nome],[...]]

    lista_separada = []
    with open("usuarios.txt", "r", encoding="utf8") as arquivo:
        lista = arquivo.readlines()
    for linha in lista:
        linha = linha.strip("\n")
        lista_separada.append(linha.split("|"))
    lista_separada.pop(0)  # Remove o modelo visual
    return lista_separada


def lista_reserva():
    # função pra colocar os dados dos arquivos em listas com o seguinte formato:

    #                    Reserva1                             Reserva2
    # lista=[[codigo,usuario,livro,data,status],[codigo,usuario,livro,data,status],[...]]

    lista_separada = []
    with open("reservas.txt", "r", encoding="utf8") as arquivo:
        lista = arquivo.readlines()
    for linha in lista:
        linha = linha.strip("\n")
        lista_separada.append(linha.split("|"))
    lista_separada.pop(0)  # Remove o modelo visual
    return lista_separada


def cadastro_livro():
    livros = lista_livro()
    codigo = len(livros)-1
    while True:
        codigo += 1
        if livros[-1][0] != codigo and livros[-1][0] < codigo:
            limpar()
            titulo = input(
                linha_composta, "Coloque o titulo do livro: ").strip(" ")
            limpar()
            autor = input(linha_composta,
                          "Coloque o nome do autor: ").strip(" ")
            limpar()
            ano_publicacao = input(
                linha_composta, "Coloque o ano que o livro foi publicado ").strip(" ")
            while ano_publicacao.isnumeric() == False and len(ano_publicacao) != 4:
                limpar()
                print(linha_composta,
                      "Valor invalido!\nUse o seguinte modelo: YYYY\n")
                ano_publicacao = input(
                    "Coloque o ano que o livro foi publicado: ").strip(" ")
            limpar()
            quantidade_exemplares = input(
                linha_composta, "Coloque a quantidade de exemplares do livro: ").strip(" ")
            while quantidade_exemplares.isnumeric() == False:
                limpar()
                print(linha_composta, "Valor invalido!\n")
                quantidade_exemplares = input(
                    "Coloque a quantidade de exemplares do livro: ").strip(" ")
            with open("livros.txt", "a", encoding="utf8") as arquivo:
                arquivo.write(
                    f"{codigo}|{titulo}|{autor}|{ano_publicacao}|{quantidade_exemplares}\n")
            limpar()
            resposta = input(
                linha_composta, "Deseja cadastrar mais um livro(sim ou não)? ").lower()
            if resposta.strip(" ")[0] == "n":
                limpar()
                input(
                    linha_composta, "Operação Finalizada!\n(aperte enter para voltar ao menu)")
                return
            elif resposta.strip(" ")[0] != "s":
                limpar()
                input(linha_composta,
                      "\n\nOpção invalida!\n(aperte enter para voltar ao menu)")
                return


def cadastro_usuario():
    usuarios = lista_usuario()
    codigo = len(usuarios)-1
    while True:
        codigo += 1
        if usuarios[-1][0] != codigo and usuarios[-1][0] < codigo:
            limpar()
            nome = input(linha_composta,
                         "\nColoque o nome do usuario: ").strip(" ")
            limpar()
            email = input(linha_composta,
                          "\nColoque o email do usuario: ").strip(" ")
            limpar()
            telefone = input(
                linha_composta, "\nColoque o telefone do usuario: ").strip(" ")
            with open("usuarios.txt", "a", encoding="utf8") as arquivo:
                arquivo.write(f"{codigo}|{nome}|{email}|{telefone}\n")
            limpar()
            resposta = input(
                linha_composta, "\nDeseja cadastrar mais um usuario(sim ou não)? ").lower()
            if resposta.strip(" ")[0] == "n":
                limpar()
                input(
                    linha_composta, "Operação Finalizada!\n(aperte enter para voltar ao menu)")
                return
            elif resposta.strip(" ")[0] != "s":
                limpar()
                input(linha_composta,
                      "Opção invalida!\n(aperte enter para voltar ao menu)")
                return


def reserva_livro():
    livros = lista_livro()
    usuarios = lista_usuario()
    reservas = lista_reserva()
    codigo = len(reservas)-1
    codigos_cadastrados_usuarios = []
    codigos_cadastrados_livros = []
    livros_atualizados = [
        "Codigo|Titulo|Autor|Ano_publicação|Quant_exemplares"]
    while True:
        codigo += 1
        # verifica se ja existe algum codigo identico
        if reservas[-1][0] != codigo and reservas[-1][0] < codigo or reservas[-1][0].isnumeric() == False:
            print(linha_composta, end="")
            for usuario in usuarios:
                # Imprime o codigo e o nome dos usuarios cadastrados sendo: usuario[0]=codigo e usuario[1]=nome
                print(f"[{usuario[0]}] - {usuario[1]}")
                codigos_cadastrados_usuarios.append(usuario[0])
            codigo_usuario = input(
                linha_composta, "Digite o codigo do usuario que deseja fazer a reserva: ").strip(" ")
            # Verifica se o codigo digitado existe no sistema
            while codigo_usuario not in codigos_cadastrados_usuarios:
                print(linha_composta, "O codigo digitado não está cadastrado!\n")
                codigo_usuario = input(
                    "Digite o codigo do usuario que deseja fazer a reserva: ").strip(" ")

            limpar()
            for livro in livros:
                # Imprime o codigo e o nome dos livros cadastrados sendo: livro[0]=codigo, livro[1]=Titulo livro[4]=Exemplares
                print(f"[{livro[0]}] - {livro[1]} | Exemplares: {livro[4]}")

                if int(livro[4]) > 0:  # Verifica se existe algum exemplar
                    codigos_cadastrados_livros.append(livro[0])

            codigo_livro = input(
                linha_composta, "Digite o codigo do livro que deseja fazer a reserva: ").strip(" ")
            # Verifica se o codigo está cadastrado e se possui exemplares
            while codigo_livro not in codigos_cadastrados_livros:
                print(
                    linha_composta, "O codigo do livro não está cadastrado ou não possui exemplares disponiveis!\n")
                codigo_livro = input(
                    "Digite o codigo do livro que deseja fazer a reserva: ").strip(" ")
            limpar()
            data = input(
                linha_composta, "Usando o seguinte modelo (01/01/2000)\nColoque a data que a reserva foi publicado: ").strip(" ")
            while True:
                try:  # Verifica se a data inserida é valida para manipulação no futuro
                    strptime(data, "%d/%m/%Y")
                    break
                except ValueError:
                    limpar()
                    print(linha_composta,
                          "Valor invalido!\nUse o seguinte modelo: 01/01/2000\n")
                    data = input(
                        "Coloque o ano que o livro foi publicado: ").strip(" ")
            for livro in livros:
                if livro[0] == codigo_livro:  # Diminui o valor do quantidade exemplares do livro
                    livro[4] = int(livro)-1
                # Adiciona as strings formatadas em uma lista
                livros_atualizados.append("|".join(livro))

            with open("livros.txt", "w", encoding="utf8") as arquivo:
                # Atualiza o valor de exemplares do livro
                arquivo.writelines(livros_atualizados)

            with open("reservas.txt", "a", encoding="utf8") as arquivo:  # Guarda os dados da reserva
                arquivo.write(
                    f"{codigo}|{codigo_usuario}|{codigo_livro}|{data}|Ativa\n")
            limpar()
            resposta = input(
                f"Deseja fazer outra reserva (sim ou não)?\n>").strip().lower()
            try:
                if resposta[0] == "n":
                    limpar()
                    input(
                        f"{linha_simples} \n\tOperação Finalizada!\n{linha_simples}\n    Pressione Enter para continuar\n{linha_simples}")
                    return
                elif resposta[0] != "s":
                    limpar()
                    input(
                        f"{linha_simples}\n\tValor invalido!\n{linha_simples}\n    Pressione Enter para continuar\n{linha_simples}")
            except IndexError:
                limpar()
                input(
                    f"{linha_simples}\n\tOpção invalida!\n{linha_simples}\n    Pressione Enter para continuar\n{linha_simples}")


def criador_menu(itens, texto):  # Serve para criar o menu por meio de um dicionario

    while True:
        limpar()
        print(f'''{linha_simples}
        {texto}
{linha_simples}''')
        for numero, item in enumerate(itens, start=1):
            print(f"[{numero}]-{item}")
        print("[0]-Sair")
        opt = input("\n>").strip(" ")
        try:
            if int(opt) in range(len(itens)+1):
                return opt
            else:
                limpar()
                input(f"""{linha_simples}
        Valor Invalido!
{linha_simples}
    Pressione Enter para continuar
{linha_simples}
""")
        except ValueError:
            limpar()
            input(f"""{linha_simples}
        Valor Invalido!
{linha_simples}
    Pressione Enter para continuar
{linha_simples}
""")
            
# função para criar a listinha de listagem:
def criador_listar(formatacao, lista):
    livros = ["Codigo", "Título", "Autor","Ano de publicação",
              "Quantidade de exemplares"]
    usuarios = ["Codigo", "Nome", "Email", "Telefone"]
    reservas = ["Codigo", "Usuario que realizou a reserva",
                "Livro que foi reservado", "Data da reserva", "Status"]
    lista_usuarios = lista_usuario()
    lista_livros = lista_livro()

    if formatacao == "reservas":  # Verifica se a formatação escolhida foi reserva pq tem q colocar o nome no lugar do codigo de livro e usuario
        for indice_lista, item in enumerate(reservas):
            if indice_lista == 1:
                for usuario in lista_usuarios:
                    if usuario[0] == lista[1]:
                        print(f'{item}: {usuario[1]}')
            elif indice_lista == 2:
                for livro in lista_livros:
                    if livro[0] == lista[2]:
                        print(f'{item}: {livro[1]}')
            else:
                print(f'{item}: {lista[indice_lista]}')

    elif formatacao == "usuarios":
        for indice_lista, item in enumerate(usuarios):
            print(f'{item}: {lista[indice_lista]}')

    elif formatacao == "livros":
        for indice_lista, item in enumerate(livros):
            print(f'{item}: {lista[indice_lista]}')

def menu_pesquisar():
    # Essas listas são utilizados para criar o menu para cada uma das opções
    livros = ["Codigo", "Título", "Autor", "Ano"]
    usuarios = ["Codigo", "Nome"]
    reservas = ["Codigo da Reserva", "Data", "Código do Livro", "Código do Usuário"]
    menu_pesquisa = ["Livros", "Usuários", "Reservas"]
    texto_menu = "Como deseja pesquisar?"

    listas_livros = lista_livro()
    listas_usuarios = lista_usuario()
    listas_reservas = lista_reserva()
    while True:
        opt = criador_menu(menu_pesquisa, "Menu Pesquisar")

        if opt == "1":#livros
            opt_livros = criador_menu(livros, texto_menu)
            
            if opt_livros == "1":#codigo
                codigo_livro=False
                codigo_busca = input("Digite o codigo que deseja buscar: ")
                for livro in listas_livros:
                    if codigo_busca == livro[0]:#verifica se existe algum livro com esse codigo
                        codigo_livro=True
                        print(linha_simples+"\n\tLivro encontrado!\n"+linha_simples)

                        criador_listar("livros", livro)
                        print(linha_simples)
                if not codigo_livro:
                    limpar()
                    print(linha_simples,  "\n Não foi encontrado nenhum livro com esse codigo")


            elif opt_livros=="2":#titulo
                titulo=False
                titulo_busca = input("Digite o titulo do livro que deseja buscar: ").strip(" ")
                limpar
                for livro in listas_livros:
                    if titulo_busca.lower() in livro[1].lower():#verifica se existe algum livro com esse titulo
                        if not titulo:
                            print(linha_simples+"\n\tLivro encontrado!\n"+linha_simples)
                        titulo=True
                        criador_listar("livros", livro)
                        print(linha_simples)

                if not titulo:
                    limpar()
                    print(linha_simples,  "\n Não foi encontrado nenhum livro com esse titulo")

            elif opt_livros=="3":#Autor
                autor=False
                autor_busca = input("Digite o autor do livro que deseja buscar: ").strip(" ")
                limpar
                for livro in listas_livros:
                    if autor_busca.lower() in livro[2].lower():#verifica se existe algum livro com esse autor
                        if not autor:
                            print(linha_simples+"\n\tLivro encontrado!\n"+linha_simples)
                        autor=True
                        criador_listar("livros", livro)
                        print(linha_simples)
                if not autor:
                    limpar()
                    print(linha_simples,  "\n Não foi encontrado nenhum livro com esse autor")
            
            
            elif opt_livros=="4":#ano_publicação
                ano=False
                ano_busca = input("Digite o autor do livro que deseja buscar: ").strip(" ")
                limpar
                for livro in listas_livros:
                    if ano_busca.lower() in livro[2].lower():#verifica se existe algum livro com esse ano de publicação
                        if not ano:
                            print(linha_simples+"\n\tLivro encontrado!\n"+linha_simples)
                        ano=True
                        criador_listar("livros", livro)
                        print(linha_simples)
                if not autor:
                    limpar()
                    print(linha_simples,  "\n Não foi encontrado nenhum livro com esse ano de publicação")
                
        
        elif opt=="2":#usuarios
            opt_usuarios=criador_menu(usuarios,texto_menu)
            if opt_usuarios == "1":#codigo
                codigo_usuario=False
                codigo_busca = input("Digite o codigo que deseja buscar: ")
                for usuario in listas_usuarios:
                    if codigo_busca == usuario[0]:#verifica se existe algum usuário com esse codigo
                        codigo_usuario=True
                        print(linha_simples+"\n\tUsuário encontrado!\n"+linha_simples)

                        criador_listar("usuarios", usuario)
                        print(linha_simples)
                if not codigo_usuario:
                    limpar()
                    print(linha_simples,  "\n Não foi encontrado nenhum usuário com esse codigo")


            elif opt_usuarios=="2":#nome
                nome=False
                nome_busca = input("Digite o nome do usuário que deseja buscar: ").strip(" ")
                limpar
                for usuario in listas_usuarios:
                    if nome_busca.lower() in usuario[1].lower():#verifica se existe algum usuario com esse nome
                        if not nome:
                            print(linha_simples+"\n\tUsuário encontrado!\n"+linha_simples)
                        nome=True
                        criador_listar("usuarios", usuario)
                        print(linha_simples)
                if not nome:
                    limpar()
                    print(linha_simples,  "\n Não foi encontrado nenhum usuário com esse nome")
            
        if opt == "3":#reservas
            opt_reservas = criador_menu(reservas, texto_menu)
            
            if opt_reservas == "1":#codigo da reserva
                codigo_reserva=False
                codigo_busca = input("Digite o codigo da reserva que deseja buscar: ")
                for reserva in listas_reservas:
                    if codigo_busca == reserva[0]:#verifica se existe alguma reserva com esse codigo
                        codigo_reserva=True
                        print(linha_simples+"\n\tReserva encontrada!\n"+linha_simples)

                        criador_listar("reservas", reserva)
                        print(linha_simples)
                if not codigo_reserva:
                    limpar()
                    print(linha_simples,  "\n Não foi encontrada nenhuma reserva com esse codigo")


            elif opt_reservas=="2":#data
                data=False
                data_busca = input("Digite a data da reserva que deseja buscar: ").strip(" ")
                limpar()
                for reserva in listas_reservas:
                    if data_busca == reserva[3]:#verifica se existe alguma reserva com essa data
                        if not data:
                            print(linha_simples+"\n\tReserva encontrada!\n"+linha_simples)
                        data=True
                        criador_listar("reservas", reserva)
                        print(linha_simples)
                if not data:
                    limpar()
                    print(linha_simples,  "\n Não foi encontrado nenhuma reserva com essa data")

            elif opt_reservas=="3":#codigo do livro
                codigo_livro=False
                livro_busca = input("Digite o codigo do livro reservado que deseja buscar: ").strip(" ")
                limpar()
                for reserva in listas_reservas:
                    if livro_busca == reserva[2]:#verifica se existe alguma reserva com o codigo digitado
                        if not codigo_livro:
                            print(linha_simples+"\n\tReserva encontrado!\n"+linha_simples)
                        codigo_livro=True
                        criador_listar("reservas", reserva)
                        print(linha_simples)
                if not codigo_livro:
                    limpar()
                    print(linha_simples,  "\n Não foi encontrado nenhuma reserva com esse codigo")
            
            
            elif opt_reservas=="4":#codigo do usuario
                codigo_usuario=False
                usuario_busca = input("Digite o codigo do usuário reservado que deseja buscar: ").strip(" ")
                limpar()
                for reserva in listas_reservas:
                    if usuario_busca == reserva[1]:#verifica se existe alguma reserva com o codigo digitado
                        if not codigo_usuario:
                            print(linha_simples+"\n\tReserva encontrado!\n"+linha_simples)
                        codigo_usuario=True
                        criador_listar("reservas", reserva)
                        print(linha_simples)
                if not codigo_usuario:
                    limpar()
                    print(linha_simples,  "\n Não foi encontrado nenhuma reserva com esse codigo")
                
        elif opt=="0":
            return
        
        resposta = input(
            f"Deseja realizar outra pesquisa (sim ou não)?\n>").strip().lower()
        try:
            if resposta[0] == "n":
                limpar()
                input(
                    f"{linha_simples} \n\tOperação Finalizada!\n{linha_simples}\n    Pressione Enter para continuar\n{linha_simples}")
                return
            elif resposta[0] != "s":
                limpar()
                input(
                    f"{linha_simples}\n\tValor invalido!\n{linha_simples}\n    Pressione Enter para continuar\n{linha_simples}")
        except IndexError:
            limpar()
            input(
                f"{linha_simples}\n\tOpção invalida!\n{linha_simples}\n    Pressione Enter para continuar\n{linha_simples}")

def menu_listagem():  # função de listagem dos dados
    # listas para formatar as listas de cada tipo de listagem:
    dicionario = ["Usuários", "Livros", "Reservas",
                  "Reservas Ativas", "Reservas finalizadas"]

    listausuarios = lista_usuario()
    listalivros = lista_livro()
    listareservas = lista_reserva()
    while True:
        limpar()
# menu para o usuario digitar a opção escolhida:
        opt = criador_menu(dicionario, "O que deseja listar?")

# listagem de todos os usuários:
        if opt == "1":
            if len(listausuarios) > 0:
                limpar()
                print(f'{linha_simples}\n\t\tUsuários\n{linha_simples}')
                for usuario in listausuarios:
                    criador_listar("usuarios", usuario)
                    print(linha_simples)
            else:
                limpar()
                print(linha_simples,  "\n Não há usuários cadastrados")

# listagem de todos os livros:
        elif opt == "2":
            if len(listalivros) > 0:
                limpar()
                print(f'{linha_simples}\n\t\tLivros\n{linha_simples}')
                for livro in listalivros:
                    criador_listar("livros", livro)
                    print(linha_simples)
            else:
                limpar()
                print(linha_simples, "\n Não há livros cadastrados")

# listagem de todas as reservas:
        elif opt == "3":
            if len(listareservas) > 0:
                limpar()
                print(f'{linha_simples}\n\t\tReservas\n{linha_simples}')
                for reserva in listareservas:
                    criador_listar("reservas", reserva)
                    print(linha_simples)
            else:
                limpar()
                print(linha_simples,  "\n Não há reservas salvas")

# listagem de todas as reservas ativas:
        elif opt == '4':
            limpar()
            reserva_ativa = False
            ativas = []
            for reserva in listareservas:
                if reserva[4] == "Ativa":
                    reserva_ativa = True
                    ativas.append(reserva)
            if reserva_ativa:
                print(f'{linha_simples}\n\t\tReservas Ativas\n{linha_simples}')
                for reserva in ativas:
                    criador_listar("reservas", reserva)
                    print(linha_simples)
            else:
                print(linha_simples,  "\n Não há reservas ativas no momento")


# listagem de todas as reservas finalizadas:
        elif opt == '5':
            limpar()
            reserva_finalizada = False
            finalizadas = []
            for reserva in listareservas:
                if reserva[4] == "Finalizada":
                    reserva_finalizada = True
                    finalizadas.append(reserva)
            if reserva_finalizada:
                for reserva in finalizadas:
                    print(
                        f'{linha_simples}\n\t\tReservas Finalizadas\n{linha_simples}')
                    criador_listar("reservas", reserva)
            else:
                print(linha_simples,  "\n Não há reservas ativas no momento")

        elif opt == "0":
            break
# Mensagem de erro se o usuário digitar algum valor invalido:
        else:
            limpar()
            input(f"""{linha_simples}
        Valor Invalido!
{linha_simples}
    Pressione Enter para continuar
{linha_simples}
""")

# Verificando se o usuário deseja realizar outra listagem;
        resposta = input(
            f"Deseja realizar outra listagem (sim ou não)?\n>").strip().lower()
        try:
            if resposta[0] == "n":
                limpar()
                input(
                    f"{linha_simples} \n\tOperação Finalizada!\n{linha_simples}\n    Pressione Enter para continuar\n{linha_simples}")
                return
            elif resposta[0] != "s":
                limpar()
                input(
                    f"{linha_simples}\n\tValor invalido!\n{linha_simples}\n    Pressione Enter para continuar\n{linha_simples}")
        except IndexError:
            limpar()
            input(
                f"{linha_simples}\n\tOpção invalida!\n{linha_simples}\n    Pressione Enter para continuar\n{linha_simples}")


def menu_alterar():
    lista = ["Usuários", "Livros", "Reservas"]
    menu_livros = ["Título","Autor", "Ano de publicação","Quantidade de Exemplares"]
    menu_usuarios = ["Nome", "Email", "Telefone"]
    menu_reservas = ["Data da reserva", "Status"]
    listausuarios = lista_usuario()
    listalivros = lista_livro()
    listareservas = lista_reserva()

    while True:
        usuarios_editados = ["Codigo|Nome|Email|Telefone"]
        livros_editados = [
            "Codigo|Titulo|Autor|Ano_publicação|Quant_exemplares"]
        reservas_editadas = ["Codigo_reserva|Usuario|Livro|Data|Status"]
        codigos = []
        limpar()
# menu para o usuario digitar a opção escolhida:
        opt = criador_menu(lista, "MENU ALTERAR")

# listagem de todos os usuários:
        if opt == "1":
            if len(listausuarios) > 0:
                limpar()
                print(f'{linha_simples}\n\t\tUsuários:\n{linha_simples}')
                for usuario in listausuarios:
                    criador_listar("usuarios", usuario)
                    codigos.append(usuario[0])
                    print(linha_simples)
                cod_usuario = input(
                    "\tEscreva o codigo do usuario que deseja alterar: ").strip(" ")
                if cod_usuario in codigos:
                    opt_usuario = criador_menu(
                        menu_usuarios, "O que deseja alterar?")
                    if opt_usuario == "1":  # nome
                        nome_novo = input(
                            f"{linha_simples}\n\t\tEscreva o novo nome: ").strip(" ")
                        for usuario in listausuarios:
                            if cod_usuario == usuario[0]:
                                usuario[1] = nome_novo
                        # Traz para formatação normal
                        usuarios_editados.append("|".join(usuario))

                    elif opt_usuario == "2":  # email
                        email_novo = input(
                            f"{linha_simples}\n\t\tEscreva o novo email: ").strip(" ")
                        for usuario in listausuarios:
                            if cod_usuario == usuario[0]:
                                usuario[2] = email_novo
                        # Traz para formatação normal
                        usuarios_editados.append("|".join(usuario))

                    elif opt_usuario == "3":  # telefone
                        tel_novo = input(
                            f"{linha_simples}\n\t\tEscreva o novo telefone: ").strip(" ")
                        for usuario in listausuarios:
                            if cod_usuario == usuario[0]:
                                usuario[3] = tel_novo
                        # Traz para formatação normal
                        usuarios_editados.append("|".join(usuario))

                    elif opt_usuario == "0":
                        pass
                    if len(usuarios_editados) > 1:
                        with open("usuarios.txt", "w", encoding="utf8") as arquivo:
                            # Atualiza o valor do usuário
                            arquivo.writelines(usuarios_editados)
                else:
                    limpar()
            else:
                limpar()
                print(linha_simples,  "\n Não há usuários cadastrados")

# listagem de todos os livros:
        elif opt == "2":
            if len(listalivros) > 0:
                limpar()
                print(f'{linha_simples}\n\t\tLivros:\n{linha_simples}')
                for livro in listalivros:
                    criador_listar("livros", livro)
                    codigos.append(livro[0])
                    print(linha_simples)
                cod_livro = input(
                    "\tEscreva o codigo do livro deseja alterar: ").strip(" ")
                if cod_livro in codigos:
                    opt_livro = criador_menu(
                        menu_livros, "O que deseja alterar?")
                    if opt_livro == "1":  # Titulo
                        limpar()
                        titulo_novo = input(
                            f"{linha_simples}\n\t\tEscreva o novo titulo: ").strip(" ")
                        for livro in listalivros:
                            if cod_livro == livro[0]:
                                livro[1] = titulo_novo
                        # Traz para formatação normal
                        livros_editados.append("|".join(livro))

                    elif opt_livro == "2":  # autor
                        limpar()
                        autor_novo = input(
                            f"{linha_simples}\n\t\tEscreva o novo autor: ").strip(" ")
                        for livro in listalivros:
                            if cod_livro == livro[0]:
                                livro[2] = autor_novo
                        # Traz para formatação normal
                        livros_editados.append("|".join(livro))

                    elif opt_livro == "3":  # ano_pub
                        limpar()
                        ano_novo = input(
                            f"{linha_simples}\n\t\tEscreva o novo ano de publicação: ").strip(" ")
                        while ano_novo.isnumeric() == False and len(ano_novo) != 4:
                            limpar()
                            print(
                                linha_composta, f"Valor invalido!\n{linha_simples}Use o seguinte modelo: YYYY\n{linha_simples}")
                            ano_novo = input(
                                "Coloque o ano que o livro foi publicado: ").strip(" ")
                        for livro in listalivros:
                            if cod_livro == livro[0]:
                                livro[3] = ano_novo
                        # Traz para formatação normal
                        livros_editados.append("|".join(livro))
                    
                    elif opt_livro == "4":  # quantidade Exemplares
                        limpar()
                        quantidade_novo = input(
                            f"{linha_simples}\n\t\tEscreva a nova quantidade de exemplares: ").strip(" ")
                        while quantidade_novo.isnumeric() == False:
                            limpar()
                            print(
                                linha_composta, f"Valor invalido!\n{linha_simples}Utilize somente números\n{linha_simples}")
                            quantidade_novo = input(
                                "Escreva a nova quantidade de exemplares: ").strip(" ")
                        for livro in listalivros:
                            if cod_livro == livro[0]:
                                livro[4] = quantidade_novo
                        # Traz para formatação normal
                        livros_editados.append("|".join(livro))

                    elif opt_livro == "0":
                        pass

                    if len(livros_editados) > 1:
                        with open("livros.txt", "w", encoding="utf8") as arquivo:
                            # Atualiza o valor do usuário
                            arquivo.writelines(livros_editados)
                else:
                    limpar()
            else:
                limpar()
                print(linha_simples, "\n Não há livros cadastrados")


# listagem de todas as reservas:
        elif opt == "3":
            if len(listareservas) > 0:
                limpar()
                print(f'{linha_simples}\n\t\tReservas:\n{linha_simples}')
                for reserva in listareservas:
                    criador_listar("reservas", reserva)
                    codigos.append(reserva[0])
                    print(linha_simples)
                cod_reserva = input(
                    "Escreva o codigo da reserva deseja alterar: ").strip(" ")
                if cod_reserva in codigos:
                    opt_reserva = criador_menu(
                        menu_reservas, "O que deseja alterar?")
                    if opt_reserva == "1":  # Data
                        limpar()
                        data_nova = input(
                            f"{linha_simples}\n\t\tEscreva a nova data: ").strip(" ")
                        while True:
                            try:  # Verifica se a data inserida é valida para manipulação no futuro
                                strptime(data_nova, "%d/%m/%Y")
                                break
                            except ValueError:
                                limpar()
                                print(
                                    linha_composta, "Valor invalido!\nUse o seguinte modelo: 01/01/2000\n")
                                data_nova = input(
                                    "Escreva a nova data: ").strip(" ")

                        for reserva in listareservas:
                            if cod_reserva == reserva[0]:
                                reserva[1] = data_nova
                        # Traz para formatação normal
                        reservas_editadas.append("|".join(reserva))

                    elif opt_reserva == "2":  # Status
                        for reserva in listareservas:
                            # se for aquele que o codigo for igual ao que o usuario colocou
                            if reserva[0] == cod_reserva:
                                if reserva[4] == "Ativa":
                                    limpar()
                                    resposta = input(
                                        f"Deseja mudar o estado da reserva para finalizada?\n>").strip().lower()
                                    try:
                                        if resposta[0] == "s":
                                            limpar()
                                            input(
                                                f"{linha_simples} \n\tOperação Finalizada!\n{linha_simples}\n    Pressione Enter para continuar\n{linha_simples}")
                                            reserva[4] = "Finalizada"
                                        elif resposta[0] != "n":
                                            limpar()
                                            input(
                                                f"{linha_simples}\n\tValor Invalido!\n{linha_simples}\n    Pressione Enter para continuar\n{linha_simples}")
                                        else:
                                            pass
                                    except IndexError:
                                        limpar()
                                        input(
                                            f"{linha_simples}\n\tValor invalido!\n{linha_simples}\n    Pressione Enter para continuar\n{linha_simples}")

                                elif reserva[4] == "Finalizada":
                                    limpar()
                                    resposta = input(
                                        f"Deseja mudar o estado da reserva para ativa?\n>").strip().lower()
                                    try:
                                        if resposta[0] == "s":
                                            limpar()
                                            input(
                                                f"{linha_simples} \n\tOperação Finalizada!\n{linha_simples}\n    Pressione Enter para continuar\n{linha_simples}")
                                            reserva[4] = "Ativa"

                                        elif resposta[0] != "n":
                                            limpar()
                                            input(
                                                f"{linha_simples}\n\tValor Invalido!\n{linha_simples}\n    Pressione Enter para continuar\n{linha_simples}")
                                        else:
                                            pass
                                    except IndexError:
                                        limpar()
                                        input(
                                            f"{linha_simples}\n\tValor invalido!\n{linha_simples}\n    Pressione Enter para continuar\n{linha_simples}")
                                # Traz para formatação normal
                                reservas_editadas.append("|".join(livro))

                    elif opt_reserva == "0":
                        pass

                    if len(reservas_editadas) > 1:
                        with open("reservas.txt", "w", encoding="utf8") as arquivo:
                            # Atualiza o valor das reservas
                            arquivo.writelines(reservas_editadas)
            else:
                limpar()
                print(linha_simples,  "\n Não há reservas salvas")

        elif opt == "0":  # Sai da operação
            break

# Verificando se o usuário deseja realizar outra listagem;
        resposta = input(
            f"Deseja fazer outra alteração (sim ou não)?\n>").strip().lower()
        try:
            if resposta[0] == "n":
                limpar()
                input(
                    f"{linha_simples} \n\tOperação Finalizada!\n{linha_simples}\n    Pressione Enter para continuar\n{linha_simples}")
                return
            elif resposta[0] != "s":
                limpar()
                input(
                    f"{linha_simples}\n\tValor invalido!\n{linha_simples}\n    Pressione Enter para continuar\n{linha_simples}")
        except IndexError:
            limpar()
            input(
                f"{linha_simples}\n\tValor invalido!\n{linha_simples}\n    Pressione Enter para continuar\n{linha_simples}")

def devolucao_livro(): # função de devolução de livros reservados
    verificador=False
    listaLivros = lista_livro()
    listaReservas = lista_reserva()
    listaUsuarios =lista_usuario()
    codigos_cadastrados_livros = []
    codigos_de_livros_vinculados_aos_usuarios = []
    codigos_de_usuarios_com_reserva_ativa = []
    livros_atualizados = ["Codigo|Titulo|Autor|Ano_publicação|Quant_exemplares\n"]
    reservas_atualizadas = ["Codigo_reserva|Usuario|Livro|Data|Status\n"]
    
    for reserva in listaReservas: 
        if reserva[4] == "Ativa": 
            verificador=True
            codigos_de_usuarios_com_reserva_ativa.append(reserva[1])
    
    if verificador == False:
        input(f"{linha_simples}\n Não há reservas ativas no momento!\n(aperte enter para voltar ao menu)")         
    
    limpar()
    print(f"{linha_simples}\n\t Usuarios com reservas ativas\n{linha_simples}")
    # lista com os codigos dos usuarios que efetuaram uma reserva
    
    for usuario in listaUsuarios:#mostra os usuarios com reservas ativas
        if usuario[0] in codigos_de_usuarios_com_reserva_ativa:
            criador_listar("usuarios", usuario)
            print(linha_simples)

    codigo_usuario = input(f"""Digite o codigo do usuario que deseja devolver o livro\n\n>""").strip(" ")
    
    if codigo_usuario not in codigos_de_usuarios_com_reserva_ativa: #verifica se o codigo do livro digitado está cadastrado   
        limpar()
        input(f"{linha_simples}\n O codigo do usuário digitado não está vinculado a uma reserva!\n(aperte enter para voltar ao menu)")         
        return

    limpar()
    print(f"{linha_simples}\n\t Livros Reservados pelo usuário\n{linha_simples}")
    for reserva in listaReservas:# mostra os livros cadastrados para o usuario
        for livro in listaLivros:
            if reserva[2]==livro[0] and reserva[1]==codigo_usuario and reserva[4]=="Ativa":
                codigos_de_livros_vinculados_aos_usuarios.append(livro[0])
                criador_listar("livros", livro)
                print(linha_simples)
    
    codigo_livro = input(f"""Digite o codigo do livro que deseja devolver  
    
>""").strip(" ")
    if codigo_livro not in codigos_de_livros_vinculados_aos_usuarios: #verifica se o codigo do livro digitado está em uma reserva feita pelo usuario
        limpar()
        input(f"{linha_simples}\nO codigo do livro digitado não está vinculado ao usuário!\n(aperte enter para voltar ao menu)")         
        return
    
    for livro in listaLivros:
        limpar()
        if livro[0] == codigo_livro:
            qnt = int(livro[4]) + 1 # adiciona +1 na quantidade de exemplares
            livro[4] = str(qnt)
    
        livros_atualizados.append(str("|".join(livro)+"\n")) # adiciona todos os valores atualizados em uma lista 
    with open("livros.txt", "w", encoding="utf8") as arquivo: # joga a lista no arquivo
        arquivo.writelines(livros_atualizados)

    for reserva in listaReservas:
        limpar()
        # Faz a verificação se o codigo do livro e a do usuario são as mesmas digitadas pelo usuario na hora de devolver
        # E só faz a devolução uma vez no caso de o usuario ter mais de uma reserva do mesmo livro
        if reserva[2] == codigo_livro and reserva[1] == codigo_usuario and reserva[4]=="Ativa" and verificador==True:
            verificador=False
            reserva[4] = "Finalizada" # atualiza o status da reserva para Finalizada
        reservas_atualizadas.append("|".join(reserva)+"\n") # adiciona todos os valores atualizados em uma lista
    
    with open("reservas.txt", "w", encoding="utf8") as arquivo:# joga a lista no arquivo
        arquivo.writelines(reservas_atualizadas)
    input(
        f"{linha_simples}\n     Operação Finalizada!\n{linha_simples}\n (aperte enter para voltar ao menu)")
    
devolucao_livro()

def criador_remover(listas, codigo, listas_atualizadas, arquivo):
        #função para remover itens dos arquivos sendo as listas = os dados do arquivo aonde se deseja retirar um item
        #codigo = O codigo do item que o usuario deseja remover
        #listas_atualizadas: formatações para retornar os itens aos arquivos de forma que fiquem bonitos
        #arquivo o arquivo que deseja fazer a remoção
        listas_atualizadas_reservas = ["Codigo_reserva|Usuario|Livro|Data|Status\n"]
        reservas = lista_reserva()
        codigos_cadastrados=[]
        verificador = False
        for lista in listas:
            codigos_cadastrados.append(lista[0]) # lista com os codigos  cadastrados
        while codigo not in codigos_cadastrados: #verifica se o codigo digitado está cadastrado   
            limpar()
            input(f"{linha_simples}\nO codigo digitado não está cadastrado!\n(aperte enter para voltar ao menu)")         
            return
        for lista in listas:
            if codigo in lista:
                listas.remove(lista)
        for lista in listas:
            listas_atualizadas.append("|".join(lista)+"\n")
        with open(arquivo, "w", encoding="utf8") as arquivo: # joga a lista no arquivo
            arquivo.writelines(listas_atualizadas)
        for reserva in reservas:
            if codigo == reserva[1] or codigo == reserva[2]:
                verificador = True
                reservas.remove(reserva)
        while verificador:
            for reserva in reservas:
                listas_atualizadas_reservas.append("|".join(reserva)+"\n")
            with open("reservas.txt", "w", encoding="utf8") as arquivo: # joga a lista no arquivo
                arquivo.writelines(listas_atualizadas_reservas)
            verificador = False
        limpar()
        input(
        f"{linha_simples}\n     Operação Finalizada!\n(aperte enter para voltar ao menu)")    

def remover():
    menu=["Livros","Usuários","Reservas"]
    livros = lista_livro()
    usuarios = lista_usuario()
    reservas = lista_reserva()

    listas_atualizadas_livros = ["Codigo|Titulo|Autor|Ano_publicação|Quant_exemplares\n"]
    listas_atualizadas_reservas = ["Codigo_reserva|Usuario|Livro|Data|Status\n"]
    listas_atualizadas_usuarios = ["Codigo|Nome|Email|Telefone\n"]
    limpar()
    opt = criador_menu(menu, "MENU REMOVER")
    if opt == "1":
        limpar()
        print(f"{linha_simples}\n\t Livros Cadastrados\n{linha_simples}")
        for livro in livros:
            criador_listar("livros", livro)
            print(linha_simples)
        codigo_livro = input(f"""Digite o codigo do livro que deseja remover  
    
>""").strip(" ")
        criador_remover(livros, codigo_livro, listas_atualizadas_livros, "livros.txt")

    elif opt == "2":
        limpar()
        print(f"{linha_simples}\n\t Usuarios Cadastrados\n{linha_simples}")
        for usuario in usuarios:
            criador_listar("usuarios", usuario)
            print(linha_simples)
        codigo_usuario = input(f"""Digite o codigo do usuário que deseja remover  
    
>""").strip(" ")
        criador_remover(usuarios, codigo_usuario, listas_atualizadas_usuarios, "usuarios.txt")

    elif opt == "3":
        limpar()
        print(f"{linha_simples}\n\t Reservas Cadastrados\n{linha_simples}")
        for reserva in reservas:
            criador_listar("reservas", reserva)
            print(linha_simples)
        codigo_reserva = input(f"""Digite o codigo da reserva que deseja remover  
    
>""").strip(" ")
        criador_remover(reservas, codigo_reserva, listas_atualizadas_reservas, "reservas.txt")


def relatorio():
    reservas=lista_reserva()
    livros=lista_livro()
    usuarios=lista_usuario()
    codigos_livros=[]
    codigos_usuarios=[]
    total_de_reservas=len(reservas)#conta a quantidade total de reservas
    reservas_ativas=0
    reservas_finalizadas=0
    quantidade_livros={}
    quantidade_usuarios={}
    limpar()
    for reserva in reservas:
        
        codigos_livros.append(reserva[2])#adiciona os codigos dos livros que efetuaram uma reserva
        codigos_usuarios.append(reserva[1])#adiciona os codigos dos usuarios que efetuaram uma reserva
        
        if reserva[4] == "Ativa":#conta a quantidade de reservas ativas
            reservas_ativas+=1
        
        elif reserva[4] == "Finalizada":#conta a quantidade de reservas finalizadas
            reservas_finalizadas+=1
    
    for livro in livros:# Conta quantas vezes cada livro foi reservado pela quantidade de vezes que o codigo apareceu
        quantidade_livros[livro[0]]=codigos_livros.count(livro[0])
            

        
    for usuario in usuarios:# Conta quantas vezes cada usuario efetuou uma reserva pela quantidade de vezes que o codigo apareceu
        quantidade_usuarios[usuario[0]]=codigos_usuarios.count(usuario[0])
        
        
    texto=f'''{linha_simples+10*"-"}\n
    Quantidade de vezes que cada livro foi reservado:\n
{linha_simples+10*"-"}'''
    
    for livro in livros:
        
        for cod_livro,quantidade in quantidade_livros.items():
            if cod_livro==livro[0]:
                texto+=f"""
O livro: {livro[1]}
Com o código: {cod_livro}
Foi reservado o total de: {quantidade} vezes
{linha_simples+10*"-"}"""

    texto+=f'''\n
    Quantidade reservas efetuadas por usuario:\n
{linha_simples+10*"-"}'''

    for usuario in usuarios:
        
        for cod_usuario,quantidade in quantidade_usuarios.items():
            if cod_usuario==usuario[0]:
                texto+=f"""
O usuário: {usuario[1]}
Com o código: {cod_usuario}
Efetuou reservas o total de: {quantidade} vezes
{linha_simples+10*"-"}"""
    
    texto+=f'''

    Dado gerais sobre as reservas:

{linha_simples+10*"-"}
A quantidade total de reservas foi: {total_de_reservas}
Sendo a quantidade de ativas de: {reservas_ativas}
E a quantidade de finalizadas de: {reservas_finalizadas}
'''
    
    input(texto+f"""{linha_simples+10*"-"} 
        Operação Finalizada!
{linha_simples+10*"-"}
    Pressione Enter para continuar
{linha_simples+10*"-"}""")