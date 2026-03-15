# Sisema de Controle de Estoque
# Diciplina : Progamação de Sistemas
# Autor     : Rodrigo Lima dos Sanos Batista
# Usuario   : rodrigobatista1705
# Data      : 24/02/2026
# Descrição : Program que mostra os prudos em estoque se estao em quatidade critica, adequada ou em excesso

estoque =[  # Cria uma lista de estoque nome dos produtos e quantidade
    {"nome": "Monitor", "quantidade": 15},
    {"nome": "Teclado", "quantidade": 3},
    {"nome": "Mouse", "quantidade": 27},
    {"nome": "Capinha", "quantidade": 30},
    {"nome": "Película", "quantidade": 4 }
]

print(" == Estoque de Produtos")

for produto in estoque: # perorre cada item da lista e os coloca em uma variavel
    nome = produto["nome"]
    quant = produto["quantidade"]
    
    if quant>20: # Testa se o produto tem uma quantidade maior que 20 se sim mostra mensagem excesso
        situacao = "Excesso"
    elif quant>=5: # Testa se o produto tem uma quantidade maior ou igual a 5 e mostra msg adequado
        situacao = "Adequado"
    else: # Se nenhuma opção anterior for atendida ele mostra a msg critica
        situacao = "Crítica"

    print(f"\nProduto  : {nome}") # devido a estar dentro do laço for vai mostrar uma tabela com todos os produtos a quantidade e situação de cada um 
    print(f"Quantidade  : {quant}")
    print(f"Situação : {situacao}\n")
    print("*" *30)


dnv = "s"
while dnv == "s": #Laço while feito parapara testar se deseja processar outro item
    print("\nDeseja processar outro produto? (s/n): ", end="")
    dnv = input().lower()
    if dnv == "s": 
        nome = input("Digite o nome de outro produto: ")
        while True:
            try:
                quant= int(input("Digite a quantidade: "))
                break
            except ValueError:
                print("Entrada inválida! Digite apenas números.")

        print()
        print("*" *30)
        print(f"\nSituação : {situacao}\n")
        print("*" *30)
