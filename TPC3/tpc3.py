import re

def somador(texto):
    # Expressão regular para identificar números, 'On', 'Off' e '='
    pattern = re.compile(r'\b(?:\d+|On|Off|=)\b', re.IGNORECASE)
    
    soma = 0
    somador_ativo = True  
    
    # Encontra todos os símbolos no texto usando a expressão regular
    for match in pattern.finditer(texto):
        token = match.group().lower()
        
        if token == 'on':
            somador_ativo = True
        elif token == 'off':
            somador_ativo = False
        elif token.isdigit() and somador_ativo:
            soma += int(token)
        elif token == '=':
            print(f"Resultado da soma: {soma}")
            soma = 0  # faz reset  à soma para a próxima sequência
        
    # Se houver algum saldo de soma restante, imprime-o
    if soma != 0:
        print(f"Resultado da soma: {soma}")

# Exemplo de uso
texto = "On 123 Off = 5 On 456 = 10 Off 789 = 15"
somador(texto)
