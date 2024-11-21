def divisor_comun(x,y):
    """
    Função que calcula o maximo divisor comun entre dois nºs
    Recebe:
        2 nºs positivos
    Devolve:
        None: se não existir nenhum
        Nº: que é o MDC
    """
    menor = x
    if y < menor:
        menor= y
    maior_divisor= None
    for i in range (x,y):
        if x % i == 0 and y % i == 0:
            maior_divisor = i
            return maior_divisor

assert divisor_comun(5,10) == None, "Não existe MDC entre 5 e 10"
assert divisor_comun(6,12) == 3, "O MDC de 6 e 12 é 3"
assert divisor_comun(12,6) == 3, "O MDC de 12 e 6 é 3 "
assert divisor_comun(12,18) == 6, "O MDC de 12 e 18 é 6"
assert divisor_comun(10,20) == 5, "O MDC de 10 e 20 é 5" 
print("A função passou o teste")