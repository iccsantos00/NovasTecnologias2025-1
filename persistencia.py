import csv
import os
from data import livros, usuarios, emprestimos, emails_usuarios

ARQUIVO_LIVROS = 'livros.csv'
ARQUIVO_USUARIOS = 'usuarios.csv'
ARQUIVO_EMPRESTIMOS = 'emprestimos.csv'

def carregar_livros():
    if os.path.exists(ARQUIVO_LIVROS):
        with open(ARQUIVO_LIVROS, mode='r', newline='', encoding='utf-8') as f:
            leitor = csv.DictReader(f)
            livros.clear()
            livros.extend(list(leitor))
    else:
        livros.clear()

def salvar_livros():
    with open(ARQUIVO_LIVROS, mode='w', newline='', encoding='utf-8') as f:
        campos = ['titulo', 'autor', 'ano', 'isbn', 'categoria']
        escritor = csv.DictWriter(f, fieldnames=campos)
        escritor.writeheader()
        for livro in livros:
            escritor.writerow(livro)

def carregar_usuarios():
    if os.path.exists(ARQUIVO_USUARIOS):
        with open(ARQUIVO_USUARIOS, mode='r', newline='', encoding='utf-8') as f:
            leitor = csv.DictReader(f)
            usuarios.clear()
            usuarios.extend(list(leitor))
            emails_usuarios.clear()
            emails_usuarios.update({usuario['email'] for usuario in usuarios})
    else:
        usuarios.clear()
        emails_usuarios.clear()

def salvar_usuarios():
    with open(ARQUIVO_USUARIOS, mode='w', newline='', encoding='utf-8') as f:
        campos = ['nome', 'email', 'id', 'tipo']
        escritor = csv.DictWriter(f, fieldnames=campos)
        escritor.writeheader()
        for usuario in usuarios:
            escritor.writerow(usuario)

def carregar_emprestimos():
    if os.path.exists(ARQUIVO_EMPRESTIMOS):
        with open(ARQUIVO_EMPRESTIMOS, mode='r', newline='', encoding='utf-8') as f:
            leitor = csv.DictReader(f)
            emprestimos.clear()
            emprestimos.extend(list(leitor))
    else:
        emprestimos.clear()

def salvar_emprestimos():
    with open(ARQUIVO_EMPRESTIMOS, mode='w', newline='', encoding='utf-8') as f:
        campos = ['isbn', 'user_id', 'data_emprestimo']
        escritor = csv.DictWriter(f, fieldnames=campos)
        escritor.writeheader()
        for emprestimo in emprestimos:
            escritor.writerow(emprestimo)

def carregar_todos():
    carregar_livros()
    carregar_usuarios()
    carregar_emprestimos()

def salvar_todos():
    salvar_livros()
    salvar_usuarios()
    salvar_emprestimos()