"""
agenda.py - Aula 23
Agenda de Contatos: classe inicial
"""

# Persitência binária

import pickle



class Contato:
    
    def __init__(self, nome, telefone, email):
        self.nome = nome
        self.telefone = telefone
        self.email = email
        
    def exibir(self):
        print(f"Nome     : {self.nome}")
        print(f"Telefone : {self.telefone}")
        print(f"E-mail   : {self.email}")
        
    def para_linha_txt(self):
        return f"{self.nome};{self.telefone};{self.email}"
    
import os
    
ARQUIVOtxt = os.path.join(os.path.dirname(__file__), "agenda.txt")    
ARQUIVObin = os.path.join(os.path.dirname(__file__), "agenda.bin")

# Função para salvar em text
        
def salvar_em_text(contatos, ARQUIVOtxt):
    with open(ARQUIVOtxt, "w", encoding="utf-8") as arquivo:
        for c in contatos:
            linha = f"{c.nome};{c.telefone};{c.email}"
            arquivo.write(linha + "\n")
    print(f"✔️  {len(contatos)} contato(s) salvo(s) em {ARQUIVOtxt}")
    
    # Função para carregar do .txt
    
def carregar_de_txt(ARQUIVOtxt):
    contatos=[]
    try:
        with open(ARQUIVOtxt, "r", encoding="utf-8") as arquivo:
            for linha in arquivo:
                linha = linha.strip()
                if not linha:
                    continue
                partes = linha.split(";")
                nome, telefone, email = partes[0], partes[1], partes[2]
                contatos.append(Contato(nome, telefone, email))
    except FileNotFoundError:
        print(f"Arquivo {ARQUIVOtxt} ainda não existe. Começando vazio.")
    return contatos    


    # Função para salvar dados usando pickle
    
def salvar_em_binario(contatos, ARQUIVObin):
    with open(ARQUIVObin, "wb") as arquivo:
        pickle.dump(contatos, arquivo)
    print(f"✔️  {len(contatos)} contato(s) salvo(s) em {ARQUIVObin}")    
    
    
    
    # Função para carregar os dadods do pickle
    
def carregar_de_binario(ARQUIVObin):
    try:
        with open(ARQUIVObin, "rb") as arquivo:
            return pickle.load(arquivo)
    except FileNotFoundError:
        print(f"Arquivo {ARQUIVObin} ainda não existe. Começando vazio.")
        return[]
   
   
   # Função para Cadastrar contato
    
def cadastrar(contatos):
    print("\n--- Novo Contato ---")
    nome = input("Nome     : ")
    telefone=input("Telefone : ")
    email=input("Email    : ")
    contatos.append(Contato(nome, telefone, email))
    print("✔️  Contato cadastrado")
   
   
    # Função para Listar contatos
    
def listar(contatos):
    if not contatos:
        print("\n(agenda vazia)")
        return
    print(f"\n--- Agenda ({len(contatos)} contatos) ---")
    for i, c in enumerate(contatos, start=1):
        print(f"\n[{i}]")
        c.exibir()
   
        
        # Função para remover contato
        
def remover (contatos):
    listar(contatos)
    if not contatos:
        return
    indice = int(input("\nN° do contato a remover: ")) -1
    if 0 <= indice < len(contatos):
        removido = contatos.pop(indice)
        print(f"✔️  Contato '{removido.nome}' removido.")
        
    else:
        print("Índice inválido.")

    
    # Função de Menu
    
def menu():
    
    contatos = carregar_de_binario(ARQUIVObin) or carregar_de_txt(ARQUIVOtxt)
    while True:
        print("\n========= AGENDA =========")
        print("1 - Cadastrar contato")
        print("2 - Listar contatos")
        print("3 - Remover contatos")
        print("4 - Salvar em .txt")
        print("5 - Salvar em binário")
        print("0 - Sair")
        
        opcao = input("Opção: ")
        
        if opcao == "1":
            cadastrar(contatos)
        elif opcao == "2":
            listar(contatos)
        elif opcao == "3":
            remover(contatos)
        elif opcao == "4":
            salvar_em_text(contatos, "agenda.txt")
        elif opcao == "5":
            salvar_em_binario(contatos, "agenda.bin")
        elif opcao == "0":
            print("Até logo!")
            break
        else:
            print("Opção inválida.")
            
if __name__=="__main__":
    menu()