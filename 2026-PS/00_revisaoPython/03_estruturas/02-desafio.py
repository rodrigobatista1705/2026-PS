# Sisema de Catalogo de Livros
# Diciplina : Progamação de Sistemas
# Autor     : Rodrigo Lima dos Sanos Batista
# Usuario   : rodrigobatista1705
# Data      : 04/03/2026
# Descrição : Catalogo de livros, cadastra um nova livro, busca por autor, contagem, mensagem quando livro não é encontrado

# Lista de Livros, nome, autor, ano, disponibilidades
catalogo =[
    {"titulo": "Arsène Lupin o Ladrão de Casaca", "autor": "Maurice Leblanc", "ano": 1907, "disponivel": True},
    {"titulo": "O Pequeno Príncipe", "autor": "Antoine de Saint-Exupéry", "ano": 1943, "disponivel": False},
    {"titulo": "Moby Dick", "autor": "Herman Melville", "ano": 1851, "disponivel": True},
    {"titulo": "Rota 66", "autor": "Caco Barcelos", "ano": 1992, "disponivel": False},
]

# Mostrar Catalogo
for i, livro in enumerate(catalogo, start=1):
    status = "Disponivel" if livro ["disponivel"] else "Emprestado"
    print(f"\n{i}  {livro['titulo']} ({livro["ano"]})")
    print(f"  Autor:  {livro['autor']} | {status}")
    print("  "+ "-" *40)
    
# Adicionar livro

opc = input("\nDeseja adicionar um livro novo? (s/n)").lower()
if opc =="s":
    titulo = input("Título: ")
    autor = input("Autor: ")
    ano = int(input("Ano: "))
    Dispo = input("Disponível? (s/n)").lower()
    
    if Dispo == "s":
        DispoV = True
    else:DispoV = False
    
    livro_novo = {
        "titulo": titulo,
        "autor": autor,
        "ano": ano,
        "disponivel": DispoV
    }
    
    catalogo.append(livro_novo)
    print("\n Livro novo adicionado")
    for i, livro in enumerate(catalogo, start=1):
        status = "Disponível" if livro["disponivel"] else "Emprestado"
        print(f"\n{i} - {livro['titulo']} ({livro['ano']})")
        print(f"  Autor: {livro['autor']} | {status}")
        print("  " + "-" * 40)
   
   
# Procurar autor e mostrar suas obras suas obras
opc2 = input("\nDeseja procurar um autor e seus livros? (s/n)").lower()
if opc2 == "s":
    print("\n+++ Busca por Autor +++")
    busca = input("Digite o nome do autor (ou parte): ").lower()
    encontrado = False
    for livro in catalogo:
        if busca in livro["autor"].lower():
            print(f'Encontrado: {livro["titulo"]} - {livro["autor"]}')
            encontrado = True
    if not encontrado:
        print ("Nenhum autor encontrado com esse termo.")
        
        
# Quantidade de Livros diponiveis e indisponiveis
Dis = 0
Emp = 0

for livro in catalogo:
    if livro["disponivel"]:
        Dis += 1
    else:
        Emp += 1

print(f"\nQuantidade de Livros\nDisponíveis: {Dis} \nEmprestados: {Emp} ")


# Lista de títulos emprestados
print("\n Livros Emprestados:")

emprestados = False

for livro in catalogo:
    if not livro["disponivel"]:
        print(f"- {livro['titulo']}")
        emprestados = True

if not emprestados:
    print("Nenhum livro está emprestado no momento.")