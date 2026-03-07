# CONVERSOR TEMPERATURA

def celsius_para_fahrenheit(celsius):
    return (celsius * 9/5) + 32 # Coverte celsius para fahrenheit

def celsius_para_kelvin(celsius):
    return celsius + 273.15 # Converte celsius para kelvin

def fahrenheit_para_celsius(fahrenheit):
    return (fahrenheit - 32) *5/9 # Converte  fahrenheit para celsius

# Constante do módulo
zero_aboluto_celsius = -273.15