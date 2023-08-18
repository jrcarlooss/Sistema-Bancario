class ContaBancaria:
    def __init__(self, saldo_inicial=0):
        self.saldo = saldo_inicial

    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            return f"Depósito de {valor} realizado. Saldo atual: {self.saldo}"
        else:
            return "Valor de depósito inválido."

    def sacar(self, valor):
        if valor > 0 and valor <= self.saldo:
            self.saldo -= valor
            return f"Saque de {valor} realizado. Saldo atual: {self.saldo}"
        else:
            return "Saldo insuficiente ou valor de saque inválido."

    def extrato(self):
        return f"Saldo atual: {self.saldo}"


def main():
    conta = ContaBancaria()

    while True:
        print("\nEscolha uma opção:")
        print("1. Depositar")
        print("2. Sacar")
        print("3. Extrato")
        print("4. Sair")

        escolha = int(input("Opção: "))

        if escolha == 1:
            valor = float(input("Digite o valor para depósito: "))
            print(conta.depositar(valor))
        elif escolha == 2:
            valor = float(input("Digite o valor para saque: "))
            print(conta.sacar(valor))
        elif escolha == 3:
            print(conta.extrato())
        elif escolha == 4:
            print("Saindo do sistema.")
            break
        else:
            print("Opção inválida. Escolha novamente.")


if __name__ == "__main__":
    main()
