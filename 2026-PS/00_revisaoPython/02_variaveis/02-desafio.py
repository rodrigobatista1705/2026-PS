# Sisema de Controle de Estoque
# Diciplina : Progamação de Sistemas
# Autor     : Rodrigo Lima dos Sanos Batista
# Usuario   : rodrigobatista1705
# Data      : 24/02/2026
# Descrição : Program que mostra os prudos em estoque se estao em quatidade critica, adequada ou em excesso

estoque =[
    {"nome": "Monitor", "quantidade": 15},
    {"nome": "Teclado", "quantidade": 3},
    {"nome": "Mouse", "quantidade": 27},
    {"nome": "Capinha", "quantidade": 30},
    {"nome": "Película", "quantidade": 4 }
]

print(" == Estoque de Produtos")

for produto in estoque:
    nome = produto["nome"]
    quant = produto["quantidade"]
    
    if quant>20:
        situacao = "Excesso"
    elif quant>=5:
        situacao = "Adequado"
    else:
        situacao = "Crítica"

    print(f"\nProduto  : {nome}")
    print(f"Quantidade  : {quant}")
    print(f"Situação : {situacao}\n")
    print("*" *30)


dnv = "s"
while dnv == "s":
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
