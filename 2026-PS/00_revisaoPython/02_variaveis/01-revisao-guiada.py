# Sisema de aprovação de alunos
# Diciplina : Progamação de Sistemas
# Autor     : Rodrigo Lima dos Sanos Batista
# Usuario   : rodrigobatista1705
# Data      : 24/02/2026
# Descrição : O programa vi processar a nota dos alunos de uma turma e determinar se ele esta aprovado ou reprovar

# Cabeçalho

#print("== Sistema e Aprovação de Alunos ==\n")

# Lista com os Alunos e suas Notas
turma = [
    {"nome": "Ana", "nota1": 8.0, "nota2": 7.5},
    {"nome": "Bruno", "nota1": 4.5, "nota2": 5.0},
    {"nome": "Caio", "nota1": 2.0, "nota2": 3.5},
    {"nome": "Rodrigo", "nota1": 10.0, "nota2": 9.5},
]

print("== Resultado da Turma ==\n")


# Usando "For" para percorrer os alunos que estão na Lista

for aluno in turma:
    nome  = aluno["nome"]
    nota1 = aluno["nota1"]
    nota2 = aluno["nota2"]
    media = (nota1 + nota2)/2 # A operação só funciona de forma corrida com o uso dos parenteses, pois sem eles a operação começaria pela divisão e não pela soma como é o correto


# Decisão para Aprovação, Reprovação ou Reprovação


    if media>=6.0:
        situacao = "Aprovado(a)"
    elif media>=4.0:
        situacao = "Recuperação"
    else:
        situacao = "Reprovado(a)"


# Mesagem que ira aparecer na tela

    print(f"\n Aluno   : {nome}")
    print(f" Média   : {media}")
    print(f"Situação : {situacao}")
    print("-" *30)

continuar = "s"
while continuar == "s":
    print("\nDeseja processar outro aluno? (s/n): ", end="")
    continuar = input().lower()
    if continuar == "s":

        nome = input('Digite o nome do aluno: ')
        nota1 = float(input("\nDigite a nota 1 (0 a 10): "))
        nota2 = float(input("Digite a nota 2 (0 a 10): "))


        # Processamento

        media = (nota1 + nota2)/2 # A operação só funciona de forma corrida com o uso dos parenteses, pois sem eles a operação começaria pela divisão e não pela soma como é o correto

        print(f'\nAluno   : {nome}') #print(f" ") permite uma impressao limpa e direta, alem de permitir acessar variaveis(com uso de colchetes)
        print(f'Nota 1  : {nota1:.1f}') # :.2f é um atalho que permite decidir o numero casas decimais que sera mostrado
        print(f'Nota 2  : {nota2:.1f}')
        print(f'Média   : {media:.2f}\n') 
        print(f"Situação : {situacao}")

        pass