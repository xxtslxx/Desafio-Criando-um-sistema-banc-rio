class Banco:
    def __init__(self):
        self.saldo = 0.0
        self.saques_realizados = []
        self.depositos_realizados = []

    def deposito(self, valor):
        self.saldo += valor
        self.depositos_realizados.append(valor)

    def saque(self, valor):
        if valor > 500.0:
            print("O valor máximo de saque é de R$ 500,00 por operação.")
            return
        if len(self.saques_realizados) >= 3:
            print("Você já realizou o máximo de saques permitidos por dia.")
            return
        if self.saldo < valor:
            print("Saldo insuficiente.")
            return

        self.saldo -= valor
        self.saques_realizados.append(valor)

    def extrato(self):
        print("Extrato:")
        if not self.saques_realizados and not self.depositos_realizados:
            print("Não foram realizadas movimentações.")
        else:
            for deposito in self.depositos_realizados:
                print(f"Depósito: R$ {deposito:.2f}")
            for saque in self.saques_realizados:
                print(f"Saque: R$ {saque:.2f}")
        print(f"Saldo atual: R$ {self.saldo:.2f}")


banco = Banco()

while True:
    print("1. Depósito")
    print("2. Saque")
    print("3. Extrato")
    print("4. Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        valor = float(input("Digite o valor do depósito: "))
        banco.deposito(valor)
    elif opcao == "2":
        valor = float(input("Digite o valor do saque: "))
        banco.saque(valor)
    elif opcao == "3":
        banco.extrato()
    elif opcao == "4":
        print("Encerrando o programa...")
        break
    else:
        print("Opção inválida. Tente novamente.")

