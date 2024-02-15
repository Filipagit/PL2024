# Abrir o ficheiro csv 
with open('emd.csv', 'r') as file:
    data = file.readlines()

# Remover cabeçalho e dividir  as linhas em colunas
data = [line.strip().split(',') for line in data[1:]]

# Criar uma lista de modalidades desportivas únicas
modalidades = sorted(set([row[8] for row in data]), key=lambda x: x.lower())


# Calcular o número total de atletas
total_atletas = len(data)

#Calcular o número de atletas aptos e inaptos
aptos = sum(1 for row in data if row[11] == 'true')
inaptos = total_atletas - aptos

#Calcular a percentagem de atletas aptos e inaptos
percentagem_aptos = (aptos / total_atletas) * 100
percentagem_inaptos = (inaptos / total_atletas) * 100

# Calcular a distribuição de atletas por escalão etário(5 anos)
escaloes_etarios = {}
for row in data:
    idade = int(row[5])
    escalao = f"[{idade // 5 * 5}-{idade // 5 * 5 + 4}]"
    escaloes_etarios[escalao] = escaloes_etarios.get(escalao, 0) + 1

# Imprimir resultados
print("Modalidades desportivas por Ordem Alfabética:")
for modalidade in modalidades:
    print(modalidade)
print("\nPercentagem de atletas aptos para a prática desportiva:", percentagem_aptos)
print("Percentagem de atletas inaptos para a prática desportiva:", percentagem_inaptos)
print("\nDistribuição de atletas por escalão etário:")
for escalao, quantidade in escaloes_etarios.items():
    print(f"{escalao}: {quantidade}")
