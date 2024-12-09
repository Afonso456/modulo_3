saldo_i= float(input("Insira o saldo inicial:"))
n_conta= int(input("Insira o numero da sua conta:"))
operacao= input("Qual a operação a fazer (L)Levantamento (D)Deposito:")
valor= float(input("Valor da operação:"))
saldo_f= saldo_i
if valor <= 0:
    print("Valor da operação não é valido")
else:
    if operacao.lower() == "l":
        saldo_f = saldo_i - valor
    elif operacao.lower() == "d":
        saldo_f = saldo_i + valor
    else:
        print("Operação invalida")
    print("Nº da conta", n_conta)
    if saldo_f < 0:
        print("O seu saldo não permite efetuar a operação")
    else:
        print("Saldo inicial", round(saldo_i))
        print(f"Saldo final", round(saldo_f))