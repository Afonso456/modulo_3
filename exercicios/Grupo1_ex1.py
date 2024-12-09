"""
Função que recebe dois parametros que calcula e mostra a soma dos numeros inteiros entre eles inclusive
"""
def somar(x1,x2):
    soma= 0
    for x in range (x1,x2 +1):
        soma= soma + x
    print(soma)
somar(1,10)
