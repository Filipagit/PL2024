import re
import json
import os

class VendingMachine:
    def __init__(self):
        self.stock = []
        self.load_stock()
        self.saldo=0 #saldo inicial da maquina

    def load_stock(self):
        if os.path.exists("stock.json"):
            with open("stock.json", "r") as file:
                self.stock = json.load(file)
            print("maq: Stock carregado.")

    def save_stock(self):
        with open("stock.json", "w") as file:
            json.dump(self.stock, file, indent=4)

    def listar_produtos(self):
        print("maq:")
        print("cod\t| nome\t\t| quantidade\t| preço")
        print("---------------------------------------")
        for produto in self.stock:
            print(f"{produto['cod']}\t| {produto['nome']}\t| {produto['quant']}\t\t| {produto['preco']}")

    def adicionar_produto(self, cod, nome, quant, preco):
        for produto in self.stock:
            if produto['cod'] == cod:
                produto['quant'] += quant
                print(f"maq: Produto {nome} adicionado ao stock existente.")
                self.save_stock()
                return
        self.stock.append({"cod": cod, "nome": nome, "quant": quant, "preco": preco})
        print(f"maq: Novo produto {nome} adicionado ao stock.")
        self.save_stock()

    def coin_insert(self, values):
        valid_coins = ["5c", "10c", "20c", "50c", "1e", "2e"]
        for value in values:
            if value not in valid_coins:
                return f"{value} - moeda inválida; saldo = {self.format_balance()}"
            self.coins.append(value)
            self.balance += self.value_to_cents(value)
        return f"saldo = {self.format_balance()}"    

    def format_balance(self):
        euros = self.saldo // 100
        centimos = self.saldo % 100
        return f"{euros}e{centimos:02d}c"

    def format_cost(self, cost):
        euros = cost // 100
        centimos = cost % 100
        return f"{euros}e{centimos:02d}c"




    def value_to_cents(self, value):
        if value.endswith("c"):
            return int(value[:-1])
        elif value.endswith("e"):
            return int(float(value[:-1]) * 100)
        else:
            return 0


   


   

    def selecionar_produto(self, codigo, saldo):
        for produto in self.stock:
            if produto['cod'] == codigo:
                if produto['quant'] > 0 and produto['preco'] <= saldo:
                    produto['quant'] -= 1
                    saldo -= produto['preco']
                    print(f"maq: Pode retirar o produto dispensado \"{produto['nome']}\"")
                    print(f"maq: Saldo = {self.formatar_moeda(saldo)}")
                    return saldo
                elif produto['quant'] == 0:
                    print("maq: Produto esgotado.")
                    return saldo
                else:
                    print(f"maq: Saldo insuficiente para satisfazer o seu pedido")
                    print(f"maq: Saldo = {self.formatar_moeda(saldo)}; Pedido = {self.formatar_moeda(produto['preco'])}")
                    return saldo
        print("maq: Produto inexistente.")
        return saldo

    def processar_comando(self, comando):
        partes = comando.split()
        if partes[0].upper() == "LISTAR":
            self.listar_produtos()
        elif partes[0].upper() == "MOEDA":
            saldo = 0
            valores = re.findall(r'\d+|\d+\.\d+', comando)  # extrai os valores da lista de moedas
            for valor in valores:
              valor_float = float(valor)
              if valor_float not in [0.05, 0.10, 0.20, 0.50, 1.0, 2.0]:
                   print(f"maq: {valor}c - moeda inválida; saldo = {saldo:.2f}")
                   return
              else:
                   saldo += valor_float
            print(f"maq: saldo = {saldo:.2f}")
        elif partes[0].upper() == "SELECIONAR":
            if len(partes) == 2:
                saldo = self.selecionar_produto(partes[1], saldo)
            else:
                print("maq: Comando SELECIONAR inválido.")
        elif partes[0].upper() == "ADICIONAR":
            if len(partes) == 5:
                cod, nome, quant, preco = partes[1], partes[2], int(partes[3]), float(partes[4])
                self.adicionar_produto(cod, nome, quant, preco)
            else:
                print("maq: Comando ADICIONAR inválido.")
        elif partes[0].upper() == "SAIR":
            print(f"maq: Pode retirar o troco: {self.formatar_moeda(saldo)}")
            print("maq: Até à próxima")
        else:
            print("maq: Comando inválido.")

# Exemplo de uso
maquina = VendingMachine()
print("maq: Bom dia. Estou disponível para atender o seu pedido.")
while True:
    comando = input(">> ")
    if comando.upper() == "SAIR":
        break
    maquina.processar_comando(comando)
