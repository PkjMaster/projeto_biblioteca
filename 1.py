linha = "\n"+"-"*40+"\n\n"
import os
def menu_pesquisar():
    os.system("cls")
    opt=input(f'''------------------------------
    Menu Pesquisar
------------------------------
[1]-Livros
[2]-Usuários
[3]-Reservas

>''').strip(" ")
    if opt == "1":
        os.system("cls")
        input(f'''------------------------------
    Como deseja pesquisar?
------------------------------
[1]-Codigo
[2]-Título
[3]-Autor
[4]-Ano

>''')
    elif opt=="2":
        os.system("cls")
        input(f'''------------------------------
    Como deseja pesquisar?
------------------------------
[1]-Codigo
[2]-Nome

>''')
    elif opt=="3":
        os.system("cls")
        input(f'''------------------------------
    Como deseja pesquisar?
------------------------------
[1]-Codigo da reserva
[2]-Data
[3]-Código do Livro
[4]-Código do Usuário

>''')
menu_pesquisar()