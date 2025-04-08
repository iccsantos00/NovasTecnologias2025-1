from persistencia import carregar_todos, salvar_todos
from livros import cadastrar_livro, listar_livros, buscar_livros
from usuarios import cadastrar_usuario, listar_usuarios
from emprestimos import emprestar_livro, listar_emprestimos
from relatorios import relatorios_estatisticas

def menu_principal():
    carregar_todos()
    while True:
        print("\n--- Sistema de Gestão de Biblioteca Digital ---")
        print("1. Cadastro de Livro")
        print("2. Listar Livros")
        print("3. Buscar Livro")
        print("4. Cadastro de Usuário")
        print("5. Listar Usuários")
        print("6. Empréstimo de Livro")
        print("7. Listar Empréstimos")
        print("8. Estatísticas e Relatórios")
        print("9. Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            cadastrar_livro()
        elif opcao == "2":
            listar_livros()
        elif opcao == "3":
            buscar_livros()
        elif opcao == "4":
            cadastrar_usuario()
        elif opcao == "5":
            listar_usuarios()
        elif opcao == "6":
            emprestar_livro()
        elif opcao == "7":
            listar_emprestimos()
        elif opcao == "8":
            relatorios_estatisticas()
        elif opcao == "9":
            print("Saindo do sistema...")
            salvar_todos()
            break
        else:
            print("Opção inválida, tente novamente.")
        salvar_todos()

if __name__ == "__main__":
    menu_principal()