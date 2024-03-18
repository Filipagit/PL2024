# PL2024
A90234-Ana Filipa da Cunha Rebelo

Métodos de Manipulação do Stock :

load_stock(): Carrega os dados do stock da máquina a partir de um ficheiro JSON  "stock.json" se existir.
save_stock(): guarda os dados do stock da máquina no ficheiro JSON.

listar_produtos(): Mostra uma lista dos produtos disponíveis na máquina, incluindo código, nome, quantidade e preço.

adicionar_produto(cod, nome, quant, preco): Adiciona um novo produto ao stock da máquina ou atualiza a quantidade se o produto já existir.

Métodos de Manipulação do Saldo :

coin_insert(values): Insere moedas na máquina e atualiza o saldo. Verifica se as moedas inseridas são válidas.

format_balance(): Formata o saldo atual em euros e centimos para exibição.

format_cost(cost): Formata o custo de um produto em euros e centimos para exibição.
value_to_cents(value): Converte o valor de uma moeda para centimos.

Método para Selecionar Produto :
Verifica se um produto selecionado está disponível, se o saldo é suficiente e permite a retirada do produto se todas as condições forem atendidas.

Método para Processar Comandos :
Analisa o comando inserido pelo utilizador e executa a operação correspondente. Os comandos possíveis são "LISTAR" (listar produtos disponíveis), "MOEDA" (inserir moedas), "SELECIONAR" (selecionar um produto), "ADICIONAR" (adicionar um novo produto ao stock) e "SAIR" (encerrar a operação da máquina).