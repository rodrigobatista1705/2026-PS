# CONVERSOR DE TEMPERATURA

def celsius_para_fahrenheit(celsius):
    return (celsius * 9/5) + 32 # Coverte celsius para fahrenheit

def celsius_para_kelvin(celsius):
    return celsius + 273.15 # Converte celsius para kelvin

def fahrenheit_para_celsius(fahrenheit):
    return (fahrenheit - 32) *5/9 # Converte  fahrenheit para celsius

# Constante do módulo
zero_aboluto_celsius = -273.15

if __name__=="__main__":
    # Este bloco só executa ao rodar temperatura.py diretamente
    # Ao ser importado por main.py, este bloco é Ignorado
    print("Testado temperatura.py...")
    print(f"100°C = {celsius_para_fahrenheit(100)}°F    (esperado: 212.0)")
    print(f"0°C   = {celsius_para_kelvin(0)} K          (esperao: 273.15)")
    print("OK!")