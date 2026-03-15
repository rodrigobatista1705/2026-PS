def linha_separadora(char="=", largura = 40):
    return char * largura

def formatar_resultado (origem, valor_original, unidae_origem, valor_convertido, unidade_destino):
    return f" {origem}: {valor_original:.2f} {unidae_origem} → {valor_convertido:.2f} {unidade_destino}"

def cabecalho_secao(titulo):
    sep = linha_separadora("-", len(titulo)+4)
    return f"\n{sep}\n  {titulo}\n{sep}"
