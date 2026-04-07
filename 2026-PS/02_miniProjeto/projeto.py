

# Agenda de contatos ou compromissos
#   O programa serve para uma clina ter uma agenda de compromissos com horario nome e telefone do cliente, e a clinica pode adicionar, excluir, atualizar e buscar os contatos e compromissos.
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
    if not os.path.exists(ARQUIVO):
        return agenda_carregada
    
    try:
        with open(ARQUIVO, "r", encoding="utf-8") as f:
            for linha in f:
                partes = linha.strip().split(SEPARADOR)
                if partes[0] == "paciente":
                    paciente = {
                        "tipo": "paciente",
                        "pessoa": partes[1],
                        "telefone": partes[2]
                    }
                    if len(partes) > 3:
                        consultas = []
                        for i in range(3, len(partes), 3):
                            consultas.append({
                                "descricao": partes[i],
                                "data": partes[i+1],
                                "hora": partes[i+2]
                            })
                        paciente["consultas"] = consultas
                    agenda_carregada.append(paciente)
    except Exception as e:
        print(f"❌ Erro ao carregar arquivo: {e}")
    return agenda_carregada




#Função salvar dados no .txt
def salvar_dados(agenda):
    try:
        with open(ARQUIVO, "w", encoding="utf-8") as f:
            for item in agenda:
                if item['tipo'] == 'paciente':
                    linha = f"paciente{SEPARADOR}{item['pessoa']}{SEPARADOR}{item['telefone']}"
                    if "consultas" in item:
                        for consulta in item["consultas"]:
                            linha += f"{SEPARADOR}{consulta['descricao']}{SEPARADOR}{consulta['data']}{SEPARADOR}{consulta['hora']}"
                    f.write(linha + "\n")
        print(f"💾 Dados salvos em '{ARQUIVO}'.")
    except IOError as e:
        print(f"❌ Erro ao salvar: {e}")





# Função Listar agenda
def listar_agenda(agenda):
    print("\n" + "=" * 50)
    print(" 🏥 AGENDA DA CLÍNICA")
    print("=" * 50)

    if not agenda:
        print(" Agenda vazia.")
        return

    for i, item in enumerate(agenda, 1):
        print(f"{i}. 👤 {item['pessoa']} - Tel: {item['telefone']}")
        if "consultas" in item:
            for c in item["consultas"]:
                print(f"    📅 Consulta: {c['descricao']} - {c['data']} às {c['hora']}")
        print("-" * 50)




# Função adicionar paciente com consulta dentro dele
def adicionar_paciente(agenda):
    nome = input("Nome do paciente: ").strip()
    telefone = input("Telefone do paciente: ").strip()
    
    if nome and telefone:
        paciente = {"tipo": "paciente", "pessoa": nome, "telefone": telefone}
        
        # Pergunta se deseja adicionar consulta
        escolha = input("Deseja agendar uma consulta para este paciente? (s/n): ").strip().lower()
        if escolha == "s":
            desc = input("Descrição da consulta: ").strip()
            data = input("Data (dd/mm/aaaa): ").strip()
            hora = input("Hora (hh:mm): ").strip()
            if desc and data and hora:
                paciente["consulta"] = {"descricao": desc, "data": data, "hora": hora}
                print(f"✅ Consulta para '{nome}' adicionada com sucesso!")
            else:
                print("❌ Campos obrigatórios da consulta não preenchidos.")
        
        agenda.append(paciente)
        salvar_dados(agenda)
        print(f"✅ Paciente '{nome}' cadastrado com sucesso!")
    else:
        print("❌ Nome e telefone são obrigatórios.")


    
    
# Função adicionar consulta a um paciente existente
def adicionar_consulta(agenda):
    listar_agenda(agenda)
    if not agenda:
        return
    
    try:
        idx = int(input("Número do paciente para adicionar consulta: ")) - 1
        if 0 <= idx < len(agenda):
            paciente = agenda[idx]
            if paciente['tipo'] == 'paciente':
                desc = input("Descrição da consulta: ").strip()
                data = input("Data (dd/mm/aaaa): ").strip()
                hora = input("Hora (hh:mm): ").strip()
                
                if desc and data and hora:
                    # cria lista de consultas se não existir
                    paciente.setdefault("consultas", []).append({
                        "descricao": desc,
                        "data": data,
                        "hora": hora
                    })
                    salvar_dados(agenda)
                    print(f"✅ Consulta adicionada para o paciente '{paciente['pessoa']}'!")
                else:
                    print("❌ Campos obrigatórios não preenchidos.")
            else:
                print("❌ O item selecionado não é um paciente.")
        else:
            print("❌ Número inválido.")
    except ValueError:
        print("❌ Digite um número válido.")


    
    
# Função buscar paciente ou consulta
def buscar_agenda(agenda):
    print("\n**📗​ Buscar na Agenda 📗​**")
    termo = input("Digite parte do nome ou descrição: ").strip().lower()
    encontrados = [i for i in agenda if termo in i.get('pessoa', '').lower() or termo in i.get('descricao', '').lower()]
    if encontrados:
        listar_agenda(encontrados)
    else:
        print("🔍 Nada encontrado.")
        
        
# Função excluir paciente ou consulta
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
        

# Função atualizar paciente ou consulta
def atualizar_agenda(agenda):
    listar_agenda(agenda)
    try:
        ia = int(input("Número do item para atualizar: ")) - 1
        if 0 <= ia < len(agenda):
            item = agenda[ia]
            print(f"Deixe em branco para manter o valor atual.")
            
            if item['tipo'] == 'paciente':
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
    print("\n📗​  Agenda de pacientes ou consultas ")
    print(f"📗​ Agenda carregada com {total} item(s).")
    
    opcoes = {
    "1": ("Listar Agenda", listar_agenda),
    "2": ("Adicionar Paciente (com consulta)", adicionar_paciente),
    "3": ("Adicionar Consulta", adicionar_consulta),
    "4": ("Buscar na Agenda", buscar_agenda),
    "5": ("Excluir item da Agenda", excluir_item),
    "6": ("Atualizar item da Agenda", atualizar_agenda),
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

--adicionar_paciente_com_consulta: Permite adicionar um novo paciente e opcionalmente uma consulta para esse paciente

--adicionar_compromisso: Permite adicionar um novo compromisso à agenda

--buscar_agenda: Permite buscar contatos ou compromissos por nome ou descrição

--excluir_item: Permite excluir um item da agenda

--atualizar_agenda: Permite atualizar os detalhes de um contato ou compromisso existente

--main: Função principal que gerencia o fluxo do programa e exibe o menu de opções para o usuário

'''
