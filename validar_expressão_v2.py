expressao = input("Insira a expressão matemática:")
def validar(expressao):
    """
    Função que recebe uma expressão para validar os ()
    A função devolve False se a expressão tiver erros de outra forma devolve True
    """
    contar= 0
    abriu= ""
    for l in expressao:
        if l == "(" or l == "[":
            contar += 1
        if l == ")" or l == "]":
            contar -= 1
            if abriu == "":
                return False
            ultimo= abriu[len(abriu)-1]
            if ultimo == "(" and l == ")" or ultimo == "[" and l == "]":
                temp= abriu
                #limpar a string para copiar todos os caracteres menos o ultimo
                abriu= ""
                for i in range(len(temp)-1):
                    abriu= abriu + temp[i]
            else:
                return False
    if abriu == "":
        return True
    return False

resultado = validar(expressao)
print(resultado)
