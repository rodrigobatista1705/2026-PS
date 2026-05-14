# Arquivo   : pet.py
# Disciplina : Programação de Sistemas
# Autor     : Rodrigo Lima dos Sanos Batista
# Usuario   : rodrigobatista1705
# Data      : 05/05/2026
# Conceito  : Classe, objeto, atributos, métodos, encapsulamento

import os
import pickle

# Arquivos de persistência
ARQUIVO = os.path.join(os.path.dirname(__file__), "arquivo.txt")
ARQUIVOB = os.path.join(os.path.dirname(__file__), "arquivo.bin")

# Funções de Persistência em TXT e Binario

def salvar_em_text(PETs, ARQUIVO):
    with open(ARQUIVO, "w", encoding="utf-8") as arquivo:
        for p in PETs:
            linha = f"{p.nome};{p.especie};{p.idade};{p.raca};{p.nomeD};{p.peso};{p.obs};{p.vacinacao}"
            arquivo.write(linha + "\n")
    print(f"✔️  {len(PETs)} pet(s) salvo(s) em {ARQUIVO}")


def carregar_de_txt(ARQUIVO):
    PETs = []
    try:
        with open(ARQUIVO, "r", encoding="utf-8") as arquivo:
            for linha in arquivo:
                linha = linha.strip()
                if not linha:
                    continue
                partes = linha.split(";")
                nome, especie, idade, raca, nomeD, peso, obs, vacinacao = partes
                PETs.append(Pet(nome, especie, int(idade), raca, nomeD, float(peso), obs, vacinacao == "True"))
    except FileNotFoundError:
        print(f"Arquivo {ARQUIVO} ainda não existe. Começando vazio.")
    return PETs


def salvar_em_binario(PETs, ARQUIVOB):
    with open(ARQUIVOB, "wb") as arquivo:
        pickle.dump(PETs, arquivo)
    print(f"✔️  {len(PETs)} pet(s) salvo(s) em {ARQUIVOB}")


def carregar_de_binario(ARQUIVOB):
    try:
        with open(ARQUIVOB, "rb") as arquivo:
            return pickle.load(arquivo)
    except FileNotFoundError:
        print(f"Arquivo {ARQUIVOB} ainda não existe. Começando vazio.")
        return []



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
        print(f"Peso           : {self.peso}")
        print(f"Observações    : {self.obs}")
        print(f"Vacinado       : {'Sim' if self.vacinacao else 'Não'}")
        print(f"Hospedado      : {'Sim' if self.hospedado else 'Não'}")
        print(f"Valor da diária: {self.calcular_diaria()} R$")
        
        
def verificar_vacinacao_pet(PETs):
    listar(PETs)
    indice = int(input("\nN° do pet para verificar vacinação: ")) - 1
    if 0 <= indice < len(PETs):
        PETs[indice].verificar_vacinacao()

def atualizar_peso_pet(PETs):
    listar(PETs)
    indice = int(input("\nN° do pet para atualizar peso: ")) - 1
    if 0 <= indice < len(PETs):
        PETs[indice].atualizar_peso()
        salvar_em_text(PETs, ARQUIVO)
        salvar_em_binario(PETs, ARQUIVOB)

def registrar_entrada_pet(PETs):
    listar(PETs)
    indice = int(input("\nN° do pet para registrar entrada: ")) - 1
    if 0 <= indice < len(PETs):
        PETs[indice].hospedado = True
        print(f"{PETs[indice].nome} entrou no hotel.")
        salvar_em_text(PETs, ARQUIVO)
        salvar_em_binario(PETs, ARQUIVOB)
    
def registrar_saida_pet(PETs):
    listar(PETs)
    indice = int(input("\nN° do pet para registrar saída: ")) - 1
    if 0 <= indice < len(PETs):
        PETs[indice].hospedado = False
        print(f"{PETs[indice].nome} saiu do hotel.")
        salvar_em_text(PETs, ARQUIVO)
        salvar_em_binario(PETs, ARQUIVOB)


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
    
    salvar_em_text(PETs, ARQUIVO)
    salvar_em_binario(PETs, ARQUIVOB)


#Função para listar os pets hospeados

def listar(PETs):
    if not PETs:
        print("\n(agenda vazia)")
        return

    print(f"\n--- Lista de Pets ({len(PETs)} registrado(s)) ---")
    for i, c in enumerate(PETs, start=1):
        print(f"[{i}] Nome: {c.nome} | Espécie: {c.especie} | Dono: {c.nomeD}")

    escolha = input("\nDeseja emitir resumo de algum pet? (s/n): ").lower()
    if escolha == "s":
        indice = int(input("Digite o número do pet: ")) - 1
        if 0 <= indice < len(PETs):
            PETs[indice].emitir_resumo()
        else:
            print("Índice inválido.")



# Função para remover um pet da lista
def remover_pet(PETs):
    listar(PETs)
    if not PETs:
        return
    indice = int(input("\nN° do pet a remover: ")) - 1
    if 0 <= indice < len(PETs):
        removido = PETs.pop(indice)
        print(f"✔️  Pet '{removido.nome}' removido.")
        salvar_em_text(PETs, ARQUIVO)
        salvar_em_binario(PETs, ARQUIVOB)
    else:
        print("Índice inválido.")


# Função do Menu Principal

def menu():
    PETs = carregar_de_binario(ARQUIVOB) or carregar_de_txt(ARQUIVO)
    while True:
        print("\n========= HOTEL PET =========")
        print("1 - Cadastrar pet")
        print("2 - Listar pets")
        print("3 - Remover pet")
        print("4 - Atualizar peso")
        print("5 - Verificar vacinação")
        print("6 - Registrar entrada no hotel")
        print("7 - Registrar saída do hotel")
        print("0 - Sair")

        opcao = input("Opção: ")

        if opcao == "1":
            cadastrar(PETs)
        elif opcao == "2":
            listar(PETs)
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
        elif opcao == "0":
            print("Até logo!")
            break
        else:
            print("Opção inválida.")

if __name__ == "__main__":
    menu()
