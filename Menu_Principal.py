from funcoes import *
while True:
    lista = ['Cadastrar', 'Reservar livro', 'Devolver livro', 'Editar dados', 'Remover dados', 'Pesquisar dados', 'Listar dados', 'Gerar relatorio']
    resposta = criador_menu(lista, "MENU BIBLIOTECA")

    if resposta == '1':
        limpar()
        menu_cadastrar()

    elif resposta == '2':
        limpar()
        reserva_livro()

    elif resposta == '3':
        limpar()
        devolucao_livro()

    elif resposta == '4':
        limpar()
        menu_alterar()
    
    elif resposta == '5':
        limpar()
        remover()
    
    elif resposta == '6':
        limpar()
        menu_pesquisar()

    elif resposta == '7':
        limpar()
        menu_listagem()

    elif resposta == '8':
        limpar()
        relatorio()
    
# FALTA COLOCAR A FUNÇÃO DE LIMPAR:
    elif resposta == '0':
        limpar()
        print("""Encerrando o programa. Tchau !!!
        
  ,d88b.d88b,
  88888888888
  `Y8888888Y'
    `Y888Y'  
      `Y'
""")
        break

    else:
        limpar()
        input(
        f"{linha_simples}\n\tValor invalido!\n{linha_simples}\n    Pressione Enter para continuar\n{linha_simples}")
