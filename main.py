#deposito ->

TT_SAQUE = 3
Saldo = 0
limite = 500
extrato = ""
saque = 0
saques_realizados = 0

menu = """
    Digite a operacao que deseja realizar

    [d] - Depositar
    [s] - Sacar
    [e] - Extrato
    [q] - Sair

"""

while True:

    opcao = input(menu)

    if opcao == "d":
        deposito = int(input("Digite o valor a ser depositado: "))
        Saldo += deposito
        extrato += f"Depósito: R$ {deposito:.2F}\n"
        print(f"Deposito realizado com sucesso! Saldo atual de {Saldo:.2f}")
        
    elif opcao == "s":
        if saques_realizados >= TT_SAQUE:
            print("Voce excedeu o numero e saques diários")
        else:
            try:
                saque = int(input("Digite o valor do saque: "))
                if saque > Saldo:
                    print("Saque maior que o saldo!")
                elif saque > limite:
                    print("Saque excedeu o valor do limte")
                elif saque < 0:
                    print("O valor deve ser positivo")    
                else:
                    Saldo -= saque
                    saques_realizados += 1;
                    extrato += f"Saque: R$ {saque:.2F}\n"
                    print(f"Saque realizado com sucesso! Saldo atual: R$ {Saldo:.2f}")
            except ValueError:
                print("entrada invalida. Digite apenas numeros.")

    elif opcao == "e":
        print("============Extrato=============")
        print(extrato)      
    elif opcao == "q":
         break
    else:
        print("operação invalida")
    