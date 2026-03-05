# Arquivo: 01b-debug.py
#Codgo com 4 erros

nome = input("Digite o nome do aluno: ") #erro imput correção input
nota1 = float(input("digite a nota 1: "))
nota2 = float(input("digite a nota 2: "))

media = (nota1+nota2)/2 # erro falta do parenteses " nota1 + nota2 "" correção (nota1 + nota2)
if media >=6.0:
    situacao = "Aprovado"
elif media>=4.0:
    situacao = "Recuperação"
else:
    situacao = "Reprovado"

print(f"Aluno: {nome} | Média: {media:.2f}  |  Situação: {situacao}") # erro pront correção print