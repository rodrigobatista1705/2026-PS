# Arquivo   : hotel_pets_v2.py
# Disciplina : Programação de Sistemas
# Autor     : Rodrigo Lima dos Sanos Batista
# Usuario   : rodrigobatista1705
# Data      : 14/05/2026
# Conceito  : Classe, objeto, atributos, métodos, encapsulamento

#import os
#import pickle
import json
from pathlib import Path

ARQUIVO_JSON = Path(__file__).parent / "Spet.json"

# Arquivos de persistência
#ARQUIVO = os.path.join(os.path.dirname(__file__), "arquivo.txt")
#ARQUIVOB = os.path.join(os.path.dirname(__file__), "arquivo.bin")


def salvar_pets(lista_pets):
    
    ARQUIVO_JSON.parent.mkdir(parents=True, exist_ok=True)

    
    lista_dicionarios = [pet.para_dicionario() for pet in lista_pets]
    with open(ARQUIVO_JSON, "w", encoding="utf-8") as arquivo:
        json.dump(lista_dicionarios, arquivo, ensure_ascii=False, indent=4)
    print(f"Dados salvos com sucesso em pets.json")


def carregar_pets():
    """
    Carrega os pets do arquivo pets.json.

    Se o arquivo ainda não existir, retorna uma lista vazia.
    """

    if not ARQUIVO_JSON.exists():
        print(f"Aviso: O arquivo {ARQUIVO_JSON} não foi encontrado. Iniciando lista vazia.")
        return []

    with open(ARQUIVO_JSON, "r", encoding="utf-8") as arquivo:
        lista_dicionarios = json.load(arquivo)

    PETs = []

    for dados in lista_dicionarios:
        pet = Pet.criar_de_dicionario(dados)
        PETs.append(pet)

    return PETs


# Classe Pet

class Pet:
    '''Agrupa dados e comportamentos de um Pet'''

    def __init__(self, nome, especie, idade, raca, nomeD, peso, obs, vacinacao):
        self.nome = nome
        self.especie = especie
        self.idade = idade
        self.raca = raca
        self.nomeD = nomeD
        self.peso = peso
        self.obs = obs
        self.vacinacao = vacinacao
        self.hospedado = False
        
    def calcular_diaria(self):
        if self.peso < 10:
            return int(10.0 * self.peso)
        elif 10 <= self.peso < 20:
            return int(10.0 * 10 + 5.0 * (self.peso - 10))
        else:
            return 60.0


    def emitir_resumo(self):
        print("\n--- Resumo do Pet ---")
        print(f"Nome do pet    : {self.nome}")
        print(f"Espécie        : {self.especie}")
        print(f"Idade          : {self.idade}")
        print(f"Raça           : {self.raca}")
        print(f"Nome do dono   : {self.nomeD}")
        print(f"Peso(kg)       : {self.peso}")
        print(f"Observações    : {self.obs}")
        print(f"Vacinado       : {'Sim' if self.vacinacao else 'Não'}")
        print(f"Hospedado      : {'Sim' if self.hospedado else 'Não'}")
        print(f"Valor da diária: {self.calcular_diaria()} R$")
        
    # quando uma função esta dentro da clase ela não pode ser acessada no menu ou seja crie uma função para o menu 
    def atualizar_peso(self):
        print(f"\npeso atual de {self.nome}: {self.peso} kg")
        novo_peso = float(input("DIgite o novo peso(kg): "))
        self.peso = novo_peso
        print(f"O peso foi atualizado para {self.peso} kg.")


    def verificar_vacinacao(self):
            '''Verifica se o pet está vacinado'''
            if self.vacinacao:
                print(f"{self.nome} está vacinado.")
            else:             
                print(f"{self.nome} não está vacinado.")
            return self.vacinacao
        
    def para_dicionario(self):
        return {
            "nome": self.nome,
            "especie": self.especie,
            "idade": self.idade,
            "raca": self.raca,
            "nomeD": self.nomeD,
            "peso": self.peso,
            "obs": self.obs,
            "vacinacao": self.vacinacao,
            "hospedado": self.hospedado
        }

    @staticmethod
    def criar_de_dicionario(dados):
        return Pet(
            dados.get("nome"),
            dados.get("especie"),
            dados.get("idade"),
            dados.get("raca", "Desconhecida"),  # valor padrão
            dados.get("nomeD"),
            dados.get("peso"),
            dados.get("obs"),
            dados.get("vacinacao", False)
        )


# atualizar peso   
def atualizar_peso_pet(PETs):
    if not PETs:
        print("\nNenhum pet cadastrado.")
        return
    listar(PETs)
    indice = int(input("\nN° do pet para atualizar o peso: ")) - 1
    if 0 <= indice < len(PETs):
        PETs[indice].atualizar_peso()
        salvar_pets(PETs)
    else:
        print("Índice inválido.")
        
        
def verificar_vacinacao_pet(PETs):
    if not PETs:
        print("\nNenhum pet cadastrado.")
        return
    listar(PETs)
    indice = int(input("\nN° do pet para verificar vacinação: ")) - 1
    if 0 <= indice < len(PETs):
        PETs[indice].verificar_vacinacao()
    else:
        print("Índice inválido.")


def registrar_entrada_pet(PETs):
    if not PETs:
        print("\nNenhum pet cadastrado.")
        return
    listar(PETs)
    indice = int(input("\nN° do pet para registrar entrada: ")) - 1
    if 0 <= indice < len(PETs):
        PETs[indice].hospedado = True
        print(f"{PETs[indice].nome} entrou no hotel.")
        salvar_pets(PETs)
    
def registrar_saida_pet(PETs):
    if not PETs:
        print("\nNenhum pet cadastrado.")
        return
    listar(PETs)
    indice = int(input("\nN° do pet para registrar saída: ")) - 1
    if 0 <= indice < len(PETs):
        PETs[indice].hospedado = False
        print(f"{PETs[indice].nome} saiu do hotel.")
        salvar_pets(PETs)

def buscar_pet(PETs):
    print("\n**🔍 Buscar na Pet 🔍**")
    termo = input("Digite parte do nome do pet: ").strip().lower()
    encontrados = []
    for pEt in PETs:
        if termo in pEt.nome.lower():
            encontrados.append(pEt)
    if encontrados:
        print(f"✅ Encontramos {len(encontrados)} resultado(s):")
        for pEt in encontrados:
            pEt.emitir_resumo()
    else:
        print("❌ Nenhum pet encontrado com esse termo.")
        
def hospedes(PETs):
    print("\n** Pets Hospedados **")
    hospedados = []
    for pet in PETs:
        if pet.hospedado:
            hospedados.append(pet)
    if not hospedados:
        print("\n Não há pets hospedado no hotel.")
        return

    print(f"\n--- Pets Hospedados no Hotel ({len(hospedados)} no momento) ---")
    for i, pet in enumerate(hospedados, start=1):
        print(f"[{i}] Nome: {pet.nome} | Espécie: {pet.especie} | Dono: {pet.nomeD}")

# Função de cadastrar pet

def cadastrar(PETs):
    print("\n--- Novo Pet ---")
    nome = input("Nome     : ")
    especie = input("Espécie  : ")
    idade = int(input("Idade    : "))
    raca = input("Raça     : ")
    nomeD = input("Nome do Dono : ")
    peso = float(input("Peso     : "))
    obs = input("Observações : ")
    vacinacao = input("Vacinado (s/n): ").lower() == "s"
    PETs.append(Pet(nome, especie, idade, raca, nomeD, peso, obs, vacinacao))
    print("✔️  Pet cadastrado")
    
    salvar_pets(PETs)


#Função para listar os pets hospeados

def listar(PETs):
    if not PETs:
        print("\n(agenda vazia)")
        return

    print(f"\n--- Lista de Pets ({len(PETs)} registrado(s)) ---")
    for i, c in enumerate(PETs, start=1):
        print(f"[{i}] Nome: {c.nome} | Espécie: {c.especie} | Dono: {c.nomeD}")



# Função para remover um pet da lista
def remover_pet(PETs):
    listar(PETs)
    if not PETs:
        return
    indice = int(input("\nN° do pet a remover: ")) - 1
    if 0 <= indice < len(PETs):
        removido = PETs.pop(indice)
        print(f"✔️  Pet '{removido.nome}' removido.")
        salvar_pets(PETs)
    else:
        print("Índice inválido.")


# Função do Menu Principal

def menu():
    PETs =  carregar_pets()
    while True:
        print("\n========= HOTEL PET =========")
        print("1 - Cadastrar pet")
        print("2 - Listar pets")
        print("3 - Remover pet")
        print("4 - Atualizar peso")
        print("5 - Verificar vacinação")
        print("6 - Registrar entrada no hotel")
        print("7 - Registrar saída do hotel")
        print("8 - Buscar Pet")
        print("9 - Hospedes")
        print("0 - Sair")

        opcao = input("Opção: ")

        if opcao == "1":
            cadastrar(PETs)
        elif opcao == "2":
            listar(PETs)
            escolha = input("\nDeseja emitir resumo de algum pet? (s/n): ").lower()
            if escolha == "s":
                indice = int(input("Digite o número do pet: ")) - 1
                if 0 <= indice < len(PETs):
                    PETs[indice].emitir_resumo()
                else:
                    print("Índice inválido.")               
        elif opcao == "3":
            remover_pet(PETs)
        elif opcao == "4":
            atualizar_peso_pet(PETs)
        elif opcao == "5":
            verificar_vacinacao_pet(PETs)
        elif opcao == "6":
            registrar_entrada_pet(PETs)
        elif opcao == "7":
            registrar_saida_pet(PETs)
        elif opcao == "8":
            buscar_pet(PETs)
        elif opcao == "9":
            hospedes(PETs)
        elif opcao == "0":
            print("Até logo!")
            break
        else:
            print("Opção inválida.")

if __name__ == "__main__":
    menu()
