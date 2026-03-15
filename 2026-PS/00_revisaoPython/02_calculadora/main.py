# Sistema de Calculadora Simples
# Diciplina : Progamação de Sistemas
# Autor     : Rodrigo Lima dos Sanos Batista
# Usuario   : rodrigobatista1705
# Data      : 24/02/2026
# Descrição : O programa realiza as tarefas de uma calculadora basicas com operações de + - / *


def menu(): # Função de Menu
    main()
    print("\nEstá é a Calculadora RLSB\n")
    
def entrada(): # FUnção de entrada
    menu()#Chama função de menu
    while True: # Laço de repetição para verificar se as entradas são inteiros
        try:
            a = int(input('Digite um valor: '))
            b = int(input('Digite outro valor: '))
            break
        except ValueError:
            print("Entrada inválida! Digite apenas números.")

    op = input('Digite a operação [ *  /  +  - ]: ' ) # Entrada de opções
    msg= f'Resultado de {a} {op} {b}' # Mensagem de resultado 1°entrada operação escolhida 2°entrada

    if op == '+': # Testa qual operação foi escolhida
        res = soma(a, b)# Chama função para realizar adição
        
    elif op =='-':# Testa qual operação foi escolhida caso não tenha sido a primeira
        res = subtração(a,b)# Chama função para realizar subtração
    
    elif op =="*":# Testa qual operação foi escolhida caso a primeira e segunda não tenham sido escolhidas
        res= multiplicação(a, b)# Chama função para realizar multiplicação
    
    elif op =='/':# Caso nenhuma operação anterior seja escolhida essa sera realizada
        if b==0: # Testa se o divisor for zero, caso seja ele manda msg de erro e para todo o codigo
            print("Erro: divisão por zero!")
            return
        res=divisão(a, b)# Chama função para realizar divisão
    else:
        print('digite um operador disponivel')
        entrada()

    saida(msg, res) # Mensagem final com os numeros digitados a operção e o resultado
    
def soma (a, b): # Função para soma
    return(a+b)

#subtração
def subtração(a, b): # Função para subtração
    return(a-b)
    
#multiplicação
def multiplicação(a, b):#FUnção para multiplicação
    return(a*b)
   
#divisão
def divisão(a, b): #FUnção para divisão
    return(a/b)
   
def saida (msg, resultado): # Função final de mensagem de saida
    print(f'{msg} = {resultado}')
entrada()

def main():
    while True:
        menu()
        escolha = input("Escolha uma opção: ")
        if escolha =='1':
            entrada()
        elif escolha == '2':
            print('Saindo... Obrigado por acessar!')
            break
        else:
            print('Opção invalida, tente novamente.')
