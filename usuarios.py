from data import usuarios, emails_usuarios

def cadastrar_usuario():
    print("\n--- Cadastro de Usuário ---")
    nome = input("Nome: ")
    email = input("E-mail: ")
    if email in emails_usuarios:
        print("Erro: E-mail já cadastrado!")
        return
    id_usuario = input("ID Único: ")
    print("Tipos de Usuário: 1 - Aluno, 2 - Professor, 3 - Visitante")
    opcao_tipo = input("Escolha o tipo de usuário (1/2/3): ")
    tipos = {"1": "Aluno", "2": "Professor", "3": "Visitante"}
    tipo = tipos.get(opcao_tipo, "Visitante")

    usuario = {'nome': nome, 'email': email, 'id': id_usuario, 'tipo': tipo}
    usuarios.append(usuario)
    emails_usuarios.add(email)
    print("Usuário cadastrado com sucesso!")

def listar_usuarios():
    print("\n--- Lista de Usuários ---")
    if not usuarios:
        print("Nenhum usuário cadastrado.")
        return
    for indice, usuario in enumerate(usuarios, 1):
        print(f"{indice}. {usuario['nome']} - {usuario['email']} | ID: {usuario['id']} | Tipo: {usuario['tipo']}")