# Sisema de Calcular a media de um estudante
# Diciplina : Progamação de Sistemas
# Autor     : Rodrigo Lima dos Sanos Batista
# Usuario   : rodrigobatista1705
# Data      : 07/03/2026
# Descrição : Calcular s média de um aluno

# Função para cabeçalho
def exibir_cabecalho():
    # Exibe cabeçalho no terminal
    print("+"*40)
    print("\n      Sistema de Cálculo de Média\n")
    print("      Rodrigo Lima dos S. Batista")
    print("+"*40)
    
'''Chama função'''
exibir_cabecalho()

def nome():
    nomes = input("\nQual seu nome: ")
nomes = nome()

def vali_input():
    while True:
        try:
            n1 = float(input("Digite sua 1° nota: "))
            n2 = float(input("Digite sua 2° nota: "))
            return n1, n2
        except ValueError:
            print("Entrada inválida! Digite apenas números.")
            
n1, n2 = vali_input()
# Função de Calcular media    
def calcular_media(n1, n2):
    med = (n1+n2)/2
    return med
res = calcular_media(n1, n2)

#Função de Verificação da Situação
def verif_situação(med):
    if med >= 6.0:
        situa = "Aprovado"
        emoji = "✅"
    elif med>=4.0 and med<=5.9:
        situa = "em Recuperação"
        emoji =  "⚠"
    else:
        situa = "Reprovado"
        emoji = "🔴"
    return situa, emoji
situa, emoji = verif_situação(res)

#Função de Relatorio
def relatorio():
    print("\n++++++ Resultado ++++++")
    print(f"Nome          : {nomes}")
    print(f"Media         : {res:.2f}")
    print(f"Você está     : {situa} {emoji}")
relatorio()