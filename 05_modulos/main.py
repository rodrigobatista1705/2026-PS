# Sisema de Conversão de Unidade
# Diciplina : Progamação de Sistemas
# Autor     : Rodrigo Lima dos Sanos Batista
# Usuario   : rodrigobatista1705
# Data      : 05/03/2026

# BLOCO 1 : STDLIB
import math
from random import randint, choice
from datetime import datetime

print("\n*** Explorando a Stdlib ***")
print(f"π = {math.pi:.4f}")
print(f"√2 = {math.sqrt(2):.4f}")
print(f"Número aleatório: {randint(1, 100)}")
print(f"Unidade sorteada: {choice(['km', 'milhas', 'metros'])}")
print(f"Agora: {datetime.now(). strftime('%d/%m/%Y %H:%M')}")

#BLOCO 2: MÓDULO PRÓPRIO
from conversores import temperatura

print("\n*** Conversão de Temperatura ***")
valor = 100.0
print(f"{valor}°C = {temperatura.celsius_para_fahrenheit(valor):.1f}°F")
print(f"{valor}°C = {temperatura.celsius_para_fahrenheit(valor):.1f} K")
print(f"Zero absoluto: {temperatura.zero_aboluto_celsius}°C")

#BLOCO 3: API LIMPA DO PACOTE

from conversores import km_para_milhas, celsius_para_fahrenheit

print('\n *** API Limpa ***')
print(f"100 km = {km_para_milhas(100):.2f} milhas")
print(f"25°C = {celsius_para_fahrenheit(25):.1f}°F")

#BLOCO 4: CAMADAS

from utils import cabecalho_secao, formatar_resultado

print(cabecalho_secao("Conversão de Temperatura"))
print(formatar_resultado("°C → K", 100, "°C", cel)