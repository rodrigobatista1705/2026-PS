

# Agenda de contatos ou compromissos
# O programa deve permitir ao usuário criar, ler, atualizar e excluir contatos ou compromissos.
#   26/03/2026
#   Autores: Rodrigo Lima dos Santos Batista, Ellis Moura e Fernando Henrique Ramos
#   Programação de Sistemas - Prof. Berssa

import os 
# Acessa a pasta do arquivo atual e cria o caminho para o arquivo de dados
ARQUIVO = os.path.join(os.path.dirname(__file__), "dados.txt")
SEPARADOR = "/"

#   Formato .txt
# Pessoa/numero/compromisso


# Função para carregar dados do .txt

def carregar_dados():
    agenda_carregada = []
    # Verifica se o arquivo existe antes de tentar ler
    if not os.path.exists(ARQUIVO):
        return agenda_carregada
    
    try:
        # Abre o arquivo para leitura e processa cada linha
        with open(ARQUIVO, "r", encoding="utf-8") as f:
            for linha in f:
                partes = linha.strip().split(SEPARADOR)
                if len(partes) == 3 and partes[0] == "contato":  #linha malformada -> pula
                    agenda_carregada.append({
                        "tipo": "contato",
                        "pessoa": partes[1],
                        "telefone": partes[2]
                })
    except Exception as e:
        print(f"❌ Erro ao carregar arquivo: {e}")
    return agenda_carregada


# Função salvar dados .txt
def salvar_dados(agenda): # Grava a lista
    try:
        # Abre o arquivo para escrita e salva cada item da agenda no formato definido
        with open(ARQUIVO, "w", encoding="utf-8") as f:
            for item in agenda:
                if item['tipo'] == 'contato':
                    linha = f"contato{SEPARADOR}{item['pessoa']}{SEPARADOR}{item['telefone']}\n"
                else:
                    linha = f"compromisso{SEPARADOR}{item['descricao']}{SEPARADOR}{item['data']}{SEPARADOR}{item['hora']}\n"
                f.write(linha)
        print(f"💾 Dados salvos em '{ARQUIVO}'.")
    except IOError as e:
        print(f"❌   Erro ao salvar: {e}")


# Função Listar agenda
def listar_agenda(agenda):
    '''Exibe todos os contatos e compromissos.'''
    print("\n"+ "=" *50)
    print(" 📒 AGENDA")
    print("=" * 50)
    
    if not agenda:
        print(" Agenda vazia.")
        return
    
    # Exibe cada item da agenda com formatação diferente para contatos e compromissos
    for i, item in enumerate(agenda, 1):
        if item['tipo'] == 'contato':
            print(f" {i}. 📞 {item['pessoa']} - {item['telefone']}")
        elif item['tipo'] == 'compromisso':
            print(f" {i}. 📅 {item['descricao']} - {item['data']} às {item['hora']}")
        print("-" * 50)  


#Função adicionar contato
def adicionar_contato(agenda):
    '''Coleta dados input e adiciona um novo contato'''
    pessoa = input("Nome: ").strip()
    
    print("Digite seu número de telefone (apenas , ex: 999999999): \n")
    telefone = input("Telefone: ").strip()
    
    if pessoa and telefone:
        agenda.append({"tipo": "contato", "pessoa": pessoa, "telefone": telefone})
        print(f"✅ Contato '{pessoa}' adicionado com sucesso!")
        salvar_dados(agenda)
    else:
        print("❌   Nome e telefone são obrigatórios.")
        return
    
    
# Função adicionar compromisso
def adicionar_compromisso(agenda):
    desc = input("Descrição: ").strip()
    data = input("Data (dd/mm/aaaa): ").strip()
    hora = input("Hora (hh:mm): ").strip()
    if desc and data and hora:
        agenda.append({"tipo": "compromisso", "descricao": desc, "data": data, "hora": hora})
        salvar_dados(agenda)
        print("✅ Compromisso agendado!")
    else:
        print("❌ Campos obrigatórios.")
    
    
# Função buscar contato ou compromisso
def buscar_agenda(agenda):
    print("\n**📒 Buscar na Agenda 📒**")
    termo = input("Digite parte do nome ou descrição: ").strip().lower()
    encontrados = [i for i in agenda if termo in i.get('pessoa', '').lower() or termo in i.get('descricao', '').lower()]
    if encontrados:
        listar_agenda(encontrados)
    else:
        print("🔍 Nada encontrado.")
        
        
# Função excluir contato ou compromisso
def excluir_item(agenda):
    listar_agenda(agenda)
    if not agenda:
        return
    try:
        ie = int(input("Número do item para excluir: ")) - 1
        if 0 <= ie < len(agenda):
            removido = agenda.pop(ie)
            salvar_dados(agenda)
            print(f"🗑️ Item removido com sucesso!")
        else:
            print("❌ Número inválido.")
    except ValueError:
        print("❌ Digite um número.")
        

# Função atualizar contato ou compromisso
def atualizar_agenda(agenda):
    listar_agenda(agenda)
    try:
        ia = int(input("Número do item para atualizar: ")) - 1
        if 0 <= ia < len(agenda):
            item = agenda[ia]
            print(f"Deixe em branco para manter o valor atual.")
            
            if item['tipo'] == 'contato':
                item['pessoa'] = input(f"Novo nome [{item['pessoa']}]: ") or item['pessoa']
                item['telefone'] = input(f"Novo telefone [{item['telefone']}]: ") or item['telefone']
            else:
                item['descricao'] = input(f"Nova desc. [{item['descricao']}]: ") or item['descricao']
                item['data'] = input(f"Nova data [{item['data']}]: ") or item['data']
                item['hora'] = input(f"Nova hora [{item['hora']}]: ") or item['hora']
            
            salvar_dados(agenda)
            print("✅ Atualizado!")
    except ValueError:
        print("❌ Entrada inválida.")
    
def main():
    agenda = carregar_dados()
    total = len(agenda) 
    print("\n📒  Agenda de contatos ou compromissos ")
    print(f"📒 Agenda carregada com {total} item(s).")
    
    opcoes = {
        "1": ("Listar agenda", listar_agenda),
        "2": ("Adicionar contato", adicionar_contato),
        "3": ("Adicionar compromisso", adicionar_compromisso),
        "4": ("Buscar na agenda", buscar_agenda),
        "5": ("Excluir item da agenda", excluir_item),
        "6": ("Atualizar item da agenda", atualizar_agenda),
        "0": ("Sair", None),
    }   
    while True:
        print("\n--- MENU ---")
        for k, v in opcoes.items():
            print(f"[{k}] {v[0]}")
        
        escolha = input("Opção: ").strip()
        
        if escolha == "0":
            break
        if escolha in opcoes:
            opcoes[escolha][1](agenda)
        else:
            print("⚠️ Opção inválida!")
        
if __name__ == "__main__":
    main()
                
            
            
''' 
Tipos de variaveis:
--String: SEPARADOR = "/"
--Lista: agenda = []
--Int: idx = int(input("Número do item para excluir: ")) - 1

Operadores:
--Atribuição: escolha == "0"
--Comparação: if escolha == "0":

Estruturas de controle:
--Condicional: if escolha == "0":
--Laço de repetição: while True:

Função
--Definição: def listar_agenda(agenda):
--Chamada: listar_agenda(encontrados)

try/except
--try: 
    telefone = input("Digite um número: ")
--except ValueError:
    print("❌ Digite um número.")
    
Arquivo.txt
--Leitura: with open(ARQUIVO, "r", encoding="utf-8") as f:
--Escrita: with open(ARQUIVO, "w", encoding="utf-
'''


'''
Uso de IA: copilot automatico do github para completar escrita  de codigos.

Uso do copilot para correção de bugs, e auxilo para encontrar melhorias(prinicpalmente na parte de entrada e salvamento de dados)

Uso de outros projetos prontos como base para construção do projeto final
'''

'''
Função de cada parte do código:

--carregar_dados: Lê os dados do arquivo .txt e carrega na agenda

--salvar_dados: Salva os dados da agenda no arquivo .txt

--listar_agenda: Exibe os contatos e compromissos da agenda

--adicionar_contato: Permite adicionar um novo contato à agenda

--adicionar_compromisso: Permite adicionar um novo compromisso à agenda

--buscar_agenda: Permite buscar contatos ou compromissos por nome ou descrição

--excluir_item: Permite excluir um item da agenda

--atualizar_agenda: Permite atualizar os detalhes de um contato ou compromisso existente

--main: Função principal que gerencia o fluxo do programa e exibe o menu de opções para o usuário

'''
