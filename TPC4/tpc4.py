import re

# Definir tokens
tokens = [
    ('SELECT', r'SELECT'),
    ('FROM', r'FROM'),
    ('WHERE', r'WHERE'),
    ('IDENTIFIER', r'[a-zA-Z_][a-zA-Z0-9_]*'),
    ('NUMBER', r'\d+'),
    ('COMMA', r','),
    ('GREATER_EQUAL', r'>='),
    ('OPERATOR', r'[>=<]'),
    ('STRING', r'\".*?\"'),
]

# Função para analisar a entrada
def lex(input_string):
    input_string = input_string.upper()  # Convertendo para maiúsculas para facilitar a análise
    tokens_found = []
    while len(input_string) > 0:
        match = None
        for token in tokens:
            token_type, token_pattern = token
            regex = re.compile(token_pattern)
            match = regex.match(input_string)
            if match:
                value = match.group(0)
                tokens_found.append((token_type, value))
                input_string = input_string[len(value):].strip()
                break
        if not match:
            print("Erro de sintaxe: Incapaz de analisar a entrada")
            break
    return tokens_found

# Testar o analisador léxico
query = "Select id, nome, salario From empregados Where salario >= 820"
tokens = lex(query)
print(tokens)
