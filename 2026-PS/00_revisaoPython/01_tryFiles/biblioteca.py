# Centralizar o nome evita erros de digitalização em todo o códio

import os
ARQUIVO = os.path.join(os.path.dirname(__file__), "biblioteca.txt")
#ARQUIVO = "biblioteca.txt"
SEPARADOR = "|" # separa campos em cada linha do .txt

# Formato de cada linha no arquivo:

#   titulo|autor|disponivel
# Exemplo:
#   Código Limpo|Robert C. Martin|False

def carregar_catalogo():
    '''Lê o .txt e reconstroi a lista de dicionarios'''
    catalogo = []
    try:
        # 'r' = leitura | encoding='utf-8' garante acenro corretos
        with open(ARQUIVO, "r", encoding="utf-8") as f:
            for linha in f:
                linha = linha.strip()
                if not linha:       # Ignora linhas vazias
                    continue
                partes = linha.split(SEPARADOR)
                if len(partes) != 3:  #linha malformada -> pula
                    continue
                titulo, autor, disponivel_str = partes
                catalogo.append({
                    "titulo":   titulo,
                    "autor":    autor,
                    # a string "True" no arquivo precisa virar bool true
                    "disponivel":   disponivel_str=="True"
                })
    except FileNotFoundError:
        pass    # Primeira execução: arquivo ainda não existe - tudo bem
    return catalogo

def salvar_catalogo(catalogo):
    '''Grava toda a lista no arquivo .txt'''
    try:
        # 'w' = write: cria se não existir, sobrescreve se existir
        with open(ARQUIVO, "w", encoding="utf-8") as f:
            for livro in catalogo:
                linha = f"{livro['titulo']}{SEPARADOR}{livro['autor']}{SEPARADOR}{livro['disponivel']}\n"
                f.write(linha)
        print(f"💾 Catálogo salvo em '{ARQUIVO}'.")
    except IOError as e:
        # IOError: disco cheio, permissão negada, etc. 
        print("❌   Erro ao alvar:  {e}")


def listar_livros(catalogo):
    '''Exxibe todos os livros com nuemeraçã e status.'''
    print("\n"+ "=" *50)
    print(" 📚CATÁLOGO DA BIBLIOTECA")
    print("=" * 50)
    
    if not catalogo:
        print(" Nenhum livro cadastrado.")
        return
    
    for i, livro in enumerate(catalogo, 1):
        status = "✅ Disponível" if livro["disponivel"] else "❌ Emprestado"
        print(f" {i}. {livro['titulo']} - {livro['autor']}  [{status}]")
        
    print("=" * 50)
    
    

def adicionar_livro(catalogo):
    """Coleta dados via input e aiciona um novo livro ao catálogo."""
    print("\n===Adicionar Novo Livro===")
    
    titulo = input("Título: ").strip()
    autor = input("Autor: ").strip()
    
    if not titulo or not autor:
        print("⚠️ Título e autor são obrigatórios.")
        return
    
    catalogo.append({
        "titulo": titulo, 
        "autor": autor,
        "disponivel": True
    })
    print(f"✅ '{titulo}' adicionado com sucesso!")
    #salv-catalogo porque será adicionado um novo livrro e deve ser mudado no arquivo .txt
    salvar_catalogo(catalogo)   


def buscar_livro(catalogo):
    print("\n===Buscar Livro===")
    termo = input("Digite parte do título: ").strip().lower()
    
    try:
        resultados = [l for l in catalogo if termo in l["titulo"].lower()]
        
        if not resultados:
            print("Nenhum livro encontrado.")
            return
        
        print(f"\n {len(resultados)} resultado(s):")
        for livro in resultados:
            status = "Disponivel" if livro["disponivel"] else "Emprestado"
            print(f"    🔹{livro['titulo']} - {livro['autor']} [{status}]")

            
    except Exception as e:
        print(f"❌    Erro ao buscar livro: {e}")
    
        
def registrar_empretimo(catalogo):
    listar_livros()
    if not catalogo:
        return
    print("\n=== Registrar Empréstimo ===")
    
    try:
        numero = int(input("Número do livro: ")) #ValueError se digitar letras
        
        if numero<1 or numero>len(catalogo):
            print("⚠️ Número fora do intervalo.")
            return
        
        livro = catalogo[numero-1] # -1 porque lista começa em 0
        
        if not livro["disponivel"]:
            print(f"⚠️ '{livro['titulo']}' já está emprestado.")
        else:
            livro["disponivel"] = False
            print(f"✅ Empréstimo de: '{livro['titulo']}' registrado.")
            #salva o catálogo porque o status do livro mudou para indisponível
            salvar_catalogo(catalogo)
            
    except ValueError:
        print("❌ Entrada inválida. Digite apenas números.")


def devolver_livro(catalogo):
    listar_livros()
    if not catalogo:
        return
    print("\n=== Registrar Devolução ===")
    
    try:
        numero = int(input("Número do livro a devolver>: ")) 
        livro = catalogo[numero-1] # IndexError se o número for negativo ou >len
        
        if livro["disponivel"]:
            print(f"⚠️ '{livro['titulo']}' já está disponível.")
        else:
            livro["disponivel"] = True
            print(f"    ✅ Devolução de: '{livro['titulo']}' registrada.")
            salvar_catalogo(catalogo)    # Salva o catálogo porque o status do livro mudou para disponível
            
    except ValueError:
        print("❌  Digite apenas números.")
    except IndexError:
        print(" ❌ Número fora da lista. Verifique os livros cadastrados.")
        
        
def menu():
    # Carrega do arquivo ao iniciar- memório persitente
    catalogo = carregar_catalogo()
    total = len(catalogo)
    print("\n📚 SISTEMA DE BIBLIOTECA -v2(com persistência)")
    print(f"{total} livro(s) carregados(s) de '{ARQUIVO}'.")
    
    opcoes = {
        "1": ("Listar livros", listar_livros),
        "2": ("Adicionar livro", adicionar_livro),
        "3": ("Buscar livro", buscar_livro),
        "4": ("Registrar empréstimo", registrar_empretimo),
        "5": ("Registrar devolução", devolver_livro),
        "0": ("Sair", None),
    }
    while True:
        print("\nOpções:")
        for chave, (descricao, _) in opcoes.items():
            print(f" [{chave}] {descricao}")
            
        try:
            escolha = input("\n Sua escolha: ").strip()
            if escolha not in opcoes:
                raise ValueError(f"Opção '{escolha}' inválida.")
            
        except ValueError as e:
            print(f"⚠️ {e}")
            continue        # Volta ao while - não executa else/finally abaixo 
        
        else:
            # Executa SOMENTE quando try termina se exceção
            if escolha == "0":
                print("\n Até logo! 📚")
                break
            _, funcao = opcoes[escolha]
            funcao(catalogo)    # passa catalogo como argumento
        
        finally:
            # Executado SEMPRE - com ou sem exceção
            # Aqui: didático. Em produção: fecha arquivos, conexões, etc.
            pass
if __name__=="__main__":
    menu()
    
    
    
'''
try:
    # codigo que pode lançar sem exceção
    numero = int(input(Digite um numero: ))

except ValueError:
    # Executado SE ocorrer ValueError no bloco Try(Entrada diferente da pedida EX: pede int e difita um string)
    print("Isso não é um número")
    
excecpt Exception as e:
    Captura qualquer outra exceção imprevista
    print(f"erro inesperado {e}")
    
else:
    # Executado SOMENTE se o try terminou em exceção
    print(f"Número recebido: {numero}")
    
finally:
    #Executado SEMPRE - com ou sem exceção
    print("Operação Concluida")
    
    
    
try     ==      Sempre(código principal)    ==      código pode falhar

except      ==      Só ocorre a exceção especifica      ==      Tratar o erro com msg adequada

else    ==      Só se o try terminou sem exceção        ==      Código que depende do sucesso do try

finally     ==      Sempre -- com ou sem exceção        ==      Liberar recurso(arquivos, conexões)
    
    
    
# Tipos de except

ValueError      ==  int("abc") - tipo correto, conteudo invalido

IndexError      ==  listar[99] - indice fora do intervalo

Exception as e      ==  qualquer outro erro - sempre por último

'''
