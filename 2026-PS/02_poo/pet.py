# Arquivo   : pet.py
# Disciplina : Programação de Sistemas
# Autor     : Rodrigo Lima dos Sanos Batista
# Usuario   : rodrigobatista1705
# Data      : 24/02/2026
# Conceito  : Classe, objeto, atributos, métodos, encapsulamento

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
        print(f"Idade       : {self.idade}")
        print(f"Nome do Dono: {self.nomeD}")
        print(f"Peso        : {self.peso}")
        print(f"Observações : {self.obs}")
        print(f"Vacinacao   : {'Sim' if self.vacinacao else 'Não'}")
        print(f"Hospedagem  : {'Sim' if self.hospedado else 'Não'}")
        
        
    def registrar_entrada(self):
        '''Registra a entrada do pet no hotel'''
        self.hospedado = True
        print(f"{self.nome} entrou no hotel.")
        
    def registrar_saida(self):
        '''Registra a saída do pet do hotel'''
        self.hospedado = False
        print(f"{self.nome} saiu do hotel.")
    
    
    def calcular_diaria(self):
        '''Calcula o valor da diária com base na idade'''
        if self.idade <= 3:
            return 50.0  
        elif self.idade <= 10:
            return 60.0 
        else:
            return 70.0         
    
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
        resumo = f"\n-----------------\n\nResumo do Pet:\nNome        : {self.nome}\nEspécie     : {self.especie}\nIdade       : {self.idade} anos\nRaça        : {self.raca}\nPeso        : {self.peso} kg\nObservações : {self.obs}\nStatus Vacinação: {'Está vacinado' if self.vacinacao else 'Não está vacinado'}\nStatus Hospedagem: {'Está hospedado' if self.hospedado else 'Não está hospedado'}\nvalor da diária: R$ {self.calcular_diaria():.2f}"
        print(resumo)
        
        
pet1 = Pet("Rex", "Cachorro", 5, "Labrador", "Maria", 20.5, "brincalhão, mas medroso", True)
pet2 = Pet("Mimi", "Gato", 2, "Siamês", "João", 4.2, "muito preguiçosa", True)
pet3 = Pet("Thor", "Cachorro", 11, "Vira-Lata", "Ana", 18.0, "muito agressivo", False)
pet4 = Pet("Luna", "Gato", 3, "Persa", "Carlos", 3.5, "muito carinhosa", True)

pet1.exibir_dados()
pet1.registrar_entrada()
pet1.verificar_vacinacao()   
pet1.emitir_resumo()


pet2.exibir_dados()
pet2.registrar_entrada()
pet2.verificar_vacinacao()   
pet2.emitir_resumo()

pet3.exibir_dados()
pet3.registrar_entrada()
pet3.verificar_vacinacao()   
pet3.emitir_resumo()

pet4.exibir_dados()
pet4.registrar_entrada()
pet4.verificar_vacinacao()
pet4.emitir_resumo()