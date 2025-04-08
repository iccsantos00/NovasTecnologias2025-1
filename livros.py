from data import livros

def cadastrar_livro():
    print("\n--- Cadastro de Livro ---")
    titulo = input("Título: ")
    autor = input("Autor: ")
    ano = input("Ano de Publicação: ")
    isbn = input("ISBN: ")
    categoria = input("Categoria: ")

    livro = {'titulo': titulo, 'autor': autor, 'ano': ano, 'isbn': isbn, 'categoria': categoria}
    livros.append(livro)
    print("Livro cadastrado com sucesso!")

def listar_livros():
    print("\n--- Lista de Livros ---")
    if not livros:
        print("Nenhum livro cadastrado.")
        return
    for indice, livro in enumerate(livros, 1):
        print(f"{indice}. {livro['titulo']} - {livro['autor']} ({livro['ano']}) | ISBN: {livro['isbn']} | Categoria: {livro['categoria']}")

def buscar_livros():
    print("\n--- Busca de Livros ---")
    print("Buscar por: 1 - Título, 2 - Autor, 3 - Categoria")
    opcao = input("Escolha uma opção (1/2/3): ")
    termo = input("Digite o termo de busca: ").lower()
    encontrado = False
    for livro in livros:
        if (opcao == "1" and termo in livro['titulo'].lower()) or \
           (opcao == "2" and termo in livro['autor'].lower()) or \
           (opcao == "3" and termo in livro['categoria'].lower()):
            print(f"{livro['titulo']} - {livro['autor']} ({livro['ano']}) | ISBN: {livro['isbn']} | Categoria: {livro['categoria']}")
            encontrado = True
    if not encontrado:
        print("Nenhum livro encontrado com esse critério.")