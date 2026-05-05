# Arquivo   : pet.py
# Disciplina : Programação de Sistemas
# Autor     : Rodrigo Lima dos Sanos Batista
# Usuario   : rodrigobatista1705
# Data      : 05/05/2026
# Conceito  : Classe, objeto, atributos, métodos, encapsulamento

from time import sleep
class Pet:
    '''Em vez e guarda os dados em um dicionario, na programação estruturaada, agora pode agrupar os dadosse comportamentos dentro e uma classe'''
    
    def __init__(self, nome, especie, idade, raca, nomeD, peso,obs, vacinacao):
        '''O método construtor . Ele é executado automaticamente quando criamos um novo objeto Pet.
        ex:
        pet1 = Pet("Rex", "Cachorro", 5)
        nome: nome do pet
        especie: espécie do pet
        idade: idade do pet'''
        
        self.nome = nome
        self.especie = especie
        self.idade = idade
        self.raca = raca
        self.nomeD = nomeD
        self.peso = peso
        self.obs = obs
        self.vacinacao = vacinacao
        self.hospedado = False
        
        
    def exibir_dados(self):
        '''Exibe os dados principais do pet'''
        
        print("\n--- Dados do Pet ---")
        print(f"Nome        : {self.nome}")
        print(f"Espécie     : {self.especie}")
        print(f"Idade       : {self.idade} anos")
        print(f"Nome Dono   : {self.nomeD}")
        print(f"Peso        : {self.peso} kg")
        print(f"Observações : {self.obs}")
        print(f"Vacinacao   : {'Sim' if self.vacinacao else 'Não'}")
        print(f"Hospedagem  : {'Sim' if self.hospedado else 'Não'}\n")
        
        
    def registrar_entrada(self):
        '''Registra a entrada do pet no hotel'''
        if self.especie.lower() == "gato":
            print(f"{self.nome} é um gato e não pode ser hospedado com outros animais.")
            self.hospedado = False
            return
        elif self.especie.lower() == "hamster":
            print(f"{self.nome} é um hamster e precisa de uma gaiola especial para hospedagem.")
            print(f"{self.nome} entrou no hotel.")
        else:
            self.hospedado = True
            print(f"{self.nome} entrou no hotel.")
        
    def registrar_saida(self):
        '''Registra a saída do pet do hotel'''
        self.hospedado = False
        print(f"{self.nome} saiu do hotel.")
    
    
    def calcular_diaria(self):
        '''Calcula o valor da diária com base no peso'''
        if self.peso < 10:
            return int(10.0 * self.peso)
        elif 10 <= self.peso and self.peso < 20:
            return int(10.0 * 10 + 5.0*(self.peso - 10))
        else:
            return 60.0         
    
    def verificar_vacinacao(self):
        '''Verifica se o pet está vacinado'''
        if self.vacinacao:
            print(f"{self.nome} está vacinado.")
        else:             
            print(f"{self.nome} não está vacinado.")
        return self.vacinacao
    
    def atualizar_peso(self, novo_peso):
        '''Atualiza o peso do pet'''
        self.peso = novo_peso
        print(f"O peso foi atualizado para {self.peso} kg.")
        
        
    def emitir_resumo(self):
        '''Emite um resumo geral do pet'''
        print("\n--- Resumo do Pet ---")
        print(f"Nome do pet    : {self.nome}")
        print(f"Espécie        : {self.especie}")
        print(f"Idade          : {self.idade}")
        print(f"Raça           : {self.raca}")
        print(f"Nome do dono   : {self.nomeD}")
        print(f"Peso           : {self.peso}")
        print(f"Observações    : {self.obs}")
        print(f"Vacinado       : {'Sim' if self.vacinacao else 'Não'}")
        print(f"Hospedado      : {'Sim' if self.hospedado else 'Não'}")
        print(f"Valor da diária: {self.calcular_diaria()} R$")
        
        
pet1 = Pet("Rex", "Cachorro", 5, "Labrador", "Maria", 20.5, "brincalhão, mas medroso", True)
pet2 = Pet("Mimi", "Gato", 2, "Siamês", "João", 4.2, "muito preguiçosa", True)
pet3 = Pet("Thor", "Cachorro", 11, "Chow-chow", "Ana", 18.0, "muito agressivo e independente", False)
pet4 = Pet("Carlinhos", "Hamster", 1, "Anão Russo", "Carlos", 0.5, "muito carinhoso", True)
pet5 = Pet("Romario", "Hamster", 2, "Anão Russo", "Rodrigo", 0.6, "muito obediente", False)

pets = [pet1, pet2, pet5]

for pet in pets:
    sleep(1)
    pet.exibir_dados()
    sleep(1)
    pet.registrar_entrada()
    sleep(1)
    pet.verificar_vacinacao()
    sleep(1)
    print("Diária: R$", pet.calcular_diaria())
    sleep(1)
    pet.emitir_resumo()
    sleep(2)

pet3.exibir_dados()
print("Diária: R$", pet3.calcular_diaria())
pet3.registrar_entrada()
pet3.verificar_vacinacao()   
pet3.registrar_saida()

pet4.exibir_dados()
pet4.registrar_entrada()
pet4.verificar_vacinacao()
pet4.atualizar_peso(0.3)
print("Diária: R$", pet4.calcular_diaria())
pet4.emitir_resumo()
pet4.registrar_saida()