# Arquivo: 01b-debug.py
# Existem 4 erros
def saudacao(nome, turno="manhã"):
    mensagem = (f"Bom {turno}, {nome}!") # Erro falta de parentesesdepois do recebe
    
saudacao("Ana")
print(saudacao("Bruno", "tarde"))
def dobrar (x):
    return x*2 # calcula mais não retorna nada = correção usar return

print("Dobro de 5:", dobrar(5))

total = 0

def incrementar():
    global total     # falta de variavel global = correção usar variavel global
    total = total + 1

incrementar()
print("Total:", total)

def contagem(n): 
    # não tem parada = correção colocar if com uma condição de parada
    if n<=0:
        return
    print(n)
    contagem(n-1)

contagem(3)