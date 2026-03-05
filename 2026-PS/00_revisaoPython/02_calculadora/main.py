def menu():
    print("Está é a Calculadora RLSB")
    print('')
def entrada(): 
    menu()
    while True:
        try:
            a = int(input('Digite um valor: '))
            b = int(input('Digite outro valor: '))
            break
        except ValueError:
            print("Entrada inválida! Digite apenas números.")

    op = input('Digite a operação [ *  /  +  - ]: ' )
    msg= f'Soma de {a} {op} {b}'

    if op == '+':
        res = soma(a, b)
    elif op =='-':
        res = subtração(a,b)
    elif op =="*":
        res= multiplicação(a, b)
    elif op =='/':
        if b==0:
            print("Erro: divisão por zero!")
            return
        res=divisão(a, b)
    else:
        print('digite um operador disponivel')
        entrada()

    saida(msg, res)
    
def soma (a, b):
    return(a+b)

#subtração
def subtração(a, b):
    return(a-b)
    
#multiplicação
def multiplicação(a, b):
    return(a*b)
   
#divisão
def divisão(a, b):
    return(a/b)
   
def saida (msg, resultado):
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
