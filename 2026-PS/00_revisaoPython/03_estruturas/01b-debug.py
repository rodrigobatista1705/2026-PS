#Arquivo: 01b-debug.py
# Existem 4 erros

catalogo = [
    {"titulo": "Código Limpo",      "autor": "Robert C. Martin", "disponivel": True},
    {"titulo": "Entendendo Algoritimos", "autor": "Aditya Bhargava", "disponivel": False},
    {"titulo": "Python Fluente", "autor": "Luciano Ramalho", "disponivel": True},
]

print("Primeiro livro:", catalogo[1]["titulo"]) # Erro falta da virgula depois da aspas duplas

print("\nLivros disponiveis:")
for livro in catalogo:
    if livro ["disponivel"]:  # Só imprime "Livros disponíveis", e verifica se o livro não esta disponivel = correção tirar o == False
        print(f' ✅{livro["titulo"]}')

total = len(catalogo)
print(f"\nTotal de livros: {total}")

for chave, valor in catalogo [0].items():  # falta o .items() se não ele só vai percorrer pela variavel chave, com o ,items() percorre as duas
    print(f"  {chave}: {valor}")

primeiro_autor = catalogo[0] ["autor"] # o erro é que autor deve ser minusculo pois se não ele fica diferente da lista e o codigo não o encontra= correção de Autor para autor
print("\nAutor do primeiro livro:", primeiro_autor)