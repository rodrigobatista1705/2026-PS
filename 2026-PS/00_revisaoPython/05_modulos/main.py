# Sisema de Conversão de Unidade
# Diciplina : Progamação de Sistemas
# Autor     : Rodrigo Lima dos Sanos Batista
# Usuario   : rodrigobatista1705
# Data      : 10/03/2026

# importa os arquivos da pasta conversores e de dentro da pasta os arquivos e de detro dos arquivos suas funçoes 
from conversores import (celsius_para_fahrenheit, celsius_para_kelvin, fahrenheit_para_celsius, km_para_milhas, milhas_para_km, metros_para_pes, quilo_para_libra, quilo_para_grama, grama_para_mlgrama)

#importa os arquivos da pasta utils e de dentro da pasta os arquivos e de detro dos arquivos suas funçoes 
from utils import cabecalho_secao, formatar_resultado, linha_separadora

# chama a função temperatura, que mostra um cabeçalho de conversores de temperatura 
def menu_temperatura():
    print(cabecalho_secao("Conversores de Temperatura"))
    valor = float(input(" Valor em °C: "))
    print(formatar_resultado("°C → °F", valor, "°C", celsius_para_fahrenheit(valor), "°F"))
    print(formatar_resultado("°C → K", valor, "°C", celsius_para_kelvin(valor), "K"))

def menu_distancia():
    print(cabecalho_secao("Conversão de Distância"))
    valor = float(input("   Valor em km: "))
    print(formatar_resultado("km → mi", valor, "km", km_para_milhas(valor), "mi"))
    print(formatar_resultado("km → pés", valor*1000, "m", metros_para_pes(valor*1000), "pés"))

def menu_peso():
    print(cabecalho_secao("Conversão de Peso"))
    valor = float(input("   Valor em quilo: "))
    print(formatar_resultado("Kg → lb", valor, "kg", quilo_para_libra(valor), "lb"))
    print(formatar_resultado("kg → g", valor, "kg", quilo_para_grama(valor), "g"))

def main():
    print(linha_separadora())
    print(" SISTEMA DE CONVERSÃO DE UNIDADE")
    print(linha_separadora())

    opcoes = {"1": menu_temperatura, "2": menu_distancia, "3": menu_peso}
    
    while True:
        print("\n   [1] Temperatura     [2] Distância     [3] Peso     [S] Sair")
        escolha = input("   Opções: ").strip()
        if escolha == "S" or escolha == "s":
            print("\nSistema encerrado.")
            break
        elif escolha in opcoes:
            opcoes[escolha]()
        else:
            print(" Opção inválida")
            
            
if __name__=="__main__":
    main()


# BLOCO 1 : STDLIB
#import math
#from random import randint, choice
#from datetime import datetime

#print("\n*** Explorando a Stdlib ***")
#print(f"π = {math.pi:.4f}")
#print(f"√2 = {math.sqrt(2):.4f}")
#print(f"Número aleatório: {randint(1, 100)}")
#print(f"Unidade sorteada: {choice(['km', 'milhas', 'metros'])}")
#print(f"Agora: {datetime.now(). strftime('%d/%m/%Y %H:%M')}")

#BLOCO 2: MÓDULO PRÓPRIO
#from conversores import temperatura

#print("\n*** Conversão de Temperatura ***")
#valor = 100.0
#print(f"{valor}°C = {temperatura.celsius_para_fahrenheit(valor):.1f}°F")
#print(f"{valor}°C = {temperatura.celsius_para_fahrenheit(valor):.1f} K")
#print(f"Zero absoluto: {temperatura.zero_aboluto_celsius}°C")

#BLOCO 3: API LIMPA DO PACOTE

#from conversores import km_para_milhas, celsius_para_fahrenheit

#print('\n *** API Limpa ***')
#print(f"100 km = {km_para_milhas(100):.2f} milhas")
#print(f"25°C = {celsius_para_fahrenheit(25):.1f}°F")

#BLOCO 4: CAMADAS

#from utils import cabecalho_secao, formatar_resultado
#from conversores import milhas_para_km, celsius_para_kelvin

#print(cabecalho_secao("Conversão de Distância"))
#print(formatar_resultado("Km → mi", 100, "Km", km_para_milhas, "mi"))
#print(formatar_resultado("Km → mi", 100, "Km", milhas_para_km(), "km"))

#print(cabecalho_secao("Conversão de Temperatura"))
#print(formatar_resultado("°C → °F", 100, "°C", celsius_para_fahrenheit(100), "°F"))
#print(formatar_resultado("°C → K", 100, "°C", celsius_para_kelvin(100), "K"))
