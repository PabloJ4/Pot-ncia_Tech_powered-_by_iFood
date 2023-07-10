
#O objetivo é implementar três operações essenciais: depósito, saque e extrato. 
#O sistema será desenvolvido para um banco que busca monetizar suas operações. 
#Durante o desafio, você terá a chance de aplicar seus conhecimentos em programação Python 
#e criar um sistema funcional que simule as operações bancárias. Prepare-se para aprimorar
#suas habilidades e demonstrar sua capacidade de desenvolver soluções práticas e eficientes.


menu = """"
[1] Depositar
[2] Sacar
[3] Extrato
[4] sair


=> """

saldo = 0
limite = 500
extrato = "  "
Numero_Saques = 0
Limite_saques = 3

while True:
    opcao = input(menu)

    if opcao == "1":
        valor =float(input("Informe o valor do Depósito: "))

        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"

        else:
            print("Operação falhou! o valor informado é inválido")

    elif opcao == "2":
        valor = float(input("Informe o valor do saque: "))

        excedeu_saldo = valor > saldo

        excedeu_limite = valor > limite

        excedeu_saques = Numero_Saques >= Limite_saques

        if excedeu_saldo:
            print("Operação falhou! Você não tem  saldo suficiente.")

        elif excedeu_limite:
            print("Operação falhou! o valor de saque excede o limite.")

        elif excedeu_saques:
            print("Operação falhou! número máximo de saque excedido.")

        elif valor>0:
            saldo -= valor  
            extrato += f"Saque: R$ {valor:.2f}\n"
            Numero_Saques += 1

        else:
            print("Operação falhou! o valor informado é inválido")

    elif opcao == "3":
        print("##########Extrato##########")
        print("Não foram  realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("###########################")

    elif opcao == "4":
        break

    else:
        print("operação inválida, por favor selecione novamente a oeração desejada")