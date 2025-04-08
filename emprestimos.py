from data import emprestimos, livros, usuarios
from datetime import datetime

def emprestar_livro():
    print("\n--- Empréstimo de Livro ---")
    isbn = input("ISBN do Livro: ")
    livro = next((l for l in livros if l['isbn'] == isbn), None)
    if not livro:
        print("Livro não encontrado!")
        return
    if any(e for e in emprestimos if e['isbn'] == isbn):
        print("Livro já está emprestado!")
        return
    id_usuario = input("ID do Usuário: ")
    usuario = next((u for u in usuarios if u['id'] == id_usuario), None)
    if not usuario:
        print("Usuário não encontrado!")
        return
    data_emprestimo = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    emprestimo = {'isbn': isbn, 'user_id': id_usuario, 'data_emprestimo': data_emprestimo}
    emprestimos.append(emprestimo)
    print("Empréstimo registrado com sucesso!")

def listar_emprestimos():
    print("\n--- Empréstimos Ativos ---")
    if not emprestimos:
        print("Nenhum empréstimo registrado.")
        return
    for indice, emprestimo in enumerate(emprestimos, 1):
        livro = next((l for l in livros if l['isbn'] == emprestimo['isbn']), None)
        titulo_livro = livro['titulo'] if livro else "Livro não encontrado"
        usuario = next((u for u in usuarios if u['id'] == emprestimo['user_id']), None)
        nome_usuario = usuario['nome'] if usuario else "Usuário não encontrado"
        print(f"{indice}. Livro: {titulo_livro} (ISBN: {emprestimo['isbn']}) - Usuário: {nome_usuario} (ID: {emprestimo['user_id']}) | Data: {emprestimo['data_emprestimo']}")
