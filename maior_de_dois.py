def maior_de_dois(x,y):
    """
    Função que recebe dois numeros e devolve o maior caso iguais devolve none 
    """
    if x == y:
        return None
    elif x > y:
        return x
    else:
        return y

assert maior_de_dois(10,5) == 10, "A função devia devolver 10"
assert maior_de_dois(10,10) == None, "A função devia devolver None porque os nºs iguais"
print("A função passou todos os testes")