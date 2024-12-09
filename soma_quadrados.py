import quadrado
def  soma_quadrados(n:int)->int:
    soma= 0
    for i in range (1,n+1):
        q= quadrado.quadrado_inteiro(i)
        soma= soma + q
    return soma

assert soma_quadrados(3) == 14, "A função devia devoler 14"
assert soma_quadrados(5) == 55, "A função devia devolver 55"
print("A função passou em todos os testes")