expressao = input("Insira a expressão matemática:")
def validar(expressao):
    """
    Função que recebe uma expressão para validar os ()
    A função devolve False se a expressão tiver erros de outra forma devolve True
    """
    contar= 0
    for i in expressao:
        if i == "(":
            contar += 1
        if i == ")":
            contar -= 1
        if contar < 0:
            return False
    if contar == 0:
        return True
    return False

resultado = validar(expressao)
print(resultado)