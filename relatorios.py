from data import livros, emprestimos, usuarios

def relatorios_estatisticas():
    print("\n--- Estatísticas e Relatórios ---")

    # 1. Quantidade de livros por categoria
    livros_por_categoria = {}
    for livro in livros:
        categoria = livro['categoria']
        livros_por_categoria[categoria] = livros_por_categoria.get(categoria, 0) + 1
    print("\nQuantidade de livros por categoria:")
    for categoria, quantidade in livros_por_categoria.items():
        print(f"{categoria}: {quantidade}")

    # 2. Quantidade de empréstimos por tipo de usuário
    emprestimos_por_tipo = {}
    for emprestimo in emprestimos:
        usuario = next((u for u in usuarios if u['id'] == emprestimo['user_id']), None)
        if usuario:
            tipo = usuario['tipo']
            emprestimos_por_tipo[tipo] = emprestimos_por_tipo.get(tipo, 0) + 1
    print("\nQuantidade de empréstimos por tipo de usuário:")
    for tipo, quantidade in emprestimos_por_tipo.items():
        print(f"{tipo}: {quantidade}")

    # 3. Livros mais emprestados
    contagem_emprestimos = {}
    for emprestimo in emprestimos:
        isbn = emprestimo['isbn']
        contagem_emprestimos[isbn] = contagem_emprestimos.get(isbn, 0) + 1
    if contagem_emprestimos:
        max_emprestimos = max(contagem_emprestimos.values())
        mais_emprestados = [isbn for isbn, contagem in contagem_emprestimos.items() if contagem == max_emprestimos]
        print("\nLivro(s) mais emprestado(s):")
        for isbn in mais_emprestados:
            livro = next((l for l in livros if l['isbn'] == isbn), None)
            if livro:
                print(f"{livro['titulo']} (ISBN: {isbn}) - Empréstimos: {max_emprestimos}")
            else:
                print(f"ISBN: {isbn} - Empréstimos: {max_emprestimos}")
    else:
        print("\nNenhum empréstimo registrado.")