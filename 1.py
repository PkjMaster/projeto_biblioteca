#AQUI É SÓ PARA TESTES


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
        linha=linha.strip("\n")
        lista_separada.append(linha.split("|"))
    lista_separada.pop(0)# Remove o modelo visual 
    return lista_separada


def lista_usuario():
    # função pra colocar os dados dos arquivos em listas com o seguinte formato:

    #         Usuario1      Usuario2
    # lista=[[codigo,nome],[codigo,nome],[...]]

    lista_separada = []
    with open("usuarios.txt", "r", encoding="utf8") as arquivo:
        lista = arquivo.readlines()
    for linha in lista:
        linha=linha.strip("\n")
        lista_separada.append(linha.split("|"))
    lista_separada.pop(0)# Remove o modelo visual 
    return lista_separada


def lista_reserva():
    # função pra colocar os dados dos arquivos em listas com o seguinte formato:

    #                    Reserva1                             Reserva2
    # lista=[[codigo,usuario,livro,data,status],[codigo,usuario,livro,data,status],[...]]

    lista_separada = []
    with open("reservas.txt", "r", encoding="utf8") as arquivo:
        lista = arquivo.readlines()
    for linha in lista:
        linha=linha.strip("\n")
        lista_separada.append(linha.split("|"))
    lista_separada.pop(0)# Remove o modelo visual 
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
            for usuario in usuarios:
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
            for livro in livros:
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

linha = "\n"+"-"*30+"\n\n"  # linha pra fazer a formatação bonitinha

# listas para formatar as listas de cada tipo de listagem:
livros=["Codigo","Título","Ano de publicação","Quantidade de exemplates"]
usuarios=["Codigo","Nome","Email","Telefone"]
reservas=["Codigo","Usuario que realizou a reserva","Código do Livro","Data da reserva", "Status"]

# função para criar a listinha de listagem:
def criador_listar(formatacao, lista, nome, contador):
    lista_usuarios=lista_usuario()
    lista_livros=lista_livro()
    print(f'{linha}\t{nome} {contador}\n{linha}',end= "")
    for indice_lista, item in enumerate(formatacao):
        if "Reserva" == nome:# Verifica se a formatação escolhida foi alguma com reservas
            if indice_lista == 1:
                for usuario in lista_usuarios:
                    if usuario[0]==lista[1]:
                        print(f'{item}: {usuario[1]}')
            elif indice_lista == 2:
                for livro in lista_livros:
                    if livro[0]==lista[2]:
                        print(f'{item}: {livro[1]}')
            else:    
                print(f'{item}: {lista[indice_lista]}')
        else:
            print(f'{item}: {lista[indice_lista]}')
        
        

def listagem(): #função de listagem dos dados
    dicionario={"1":"Usuários","2":"Livros","3":"Reservas","4":"Reservas Ativas","5":"Reservas finalizadas"}
    listausuarios=lista_usuario()
    listalivros=lista_livro()
    listareservas=lista_reserva()
    linha = ('-'*35)
    while True:
        contador=1
        limpar()
# menu para o usuario digitar a opção escolhida:
        opt=criador_menu(dicionario,"O que deseja listar?")
        
# listagem de todos os usuários:
        if opt == "1":
            if len(listausuarios) > 0:
                limpar()
                for usuario in listausuarios:
                    criador_listar(usuarios, usuario, "Usuário", contador)
                    contador+=1
            else:
                limpar()
                print(linha,  "\n Não há usuários cadastrados")
               
# listagem de todos os livros:
        elif opt=="2":
            if len(listalivros) > 0:
                limpar()
                for livro in listalivros:
                    criador_listar(livros, livro, "Livro", contador)
                    contador+=1
            else:
                limpar()
                print(linha, "\n Não há livros cadastrados")
               
# listagem de todas as reservas:
        elif opt=="3":
            if len(listareservas) > 0:
                limpar()
                for reserva in listareservas:
                    criador_listar(reservas, reserva, "Reserva", contador)
                    contador+=1
            else:
                limpar()
                print(linha,  "\n Não há reservas salvas")
       
# listagem de todas as reservas ativas:
        elif opt == '4':
            limpar()
            reserva_ativa = False
            for reserva in listareservas:
                if reserva[4].strip() == "Ativa":
                    reserva_ativa = True
                    criador_listar(reservas, reserva, "Reserva", contador)
                    contador+=1
            if not reserva_ativa:
                print(linha,  "\n Não há reservas ativas no momento")

# listagem de todas as reservas finalizadas:
        elif opt == '5':
            reserva_finalizada = False
            limpar()
            for reserva in listareservas:
                if reserva[4].strip() == "Finalizada":
                    reserva_finalizada = True
                    criador_listar(reservas, reserva, "Reserva", contador)
                    contador+=1
            if not reserva_finalizada:
                print(linha, "\n Não há reservas finalizadas no momento")
                   
# Mensagem de erro se o usuário digitar algum valor invalido:
        else:
            limpar()
            input(f"""{linha}
        Valor Invalido!
{linha}
    Pressione Enter para continuar
{linha}
""")
           
# Verificando se o usuário deseja realizar outra listagem;
        resposta = input(f"\n{linha}\nDeseja realizar outra listagem (sim ou não)?\n>").strip().lower()
        try:
            if resposta[0] == "n":
                limpar()
                input(f"\n{linha} \n\tOperação Finalizada!\n{linha}\n    Pressione Enter para continuar\n{linha}")
                return
            elif resposta[0] != "s":
                limpar()
                input(f"{linha}\n\tValor invalido!\n{linha}\n    Pressione Enter para continuar\n{linha}")
        except IndexError:
            limpar()
            input(f"{linha}\n\tValor invalido!\n{linha}\n    Pressione Enter para continuar\n{linha}")