#Função que recebe  um  numero e indica se é primo ou não
def primo(n):
    """
    Função que indica se um nº é primo ou não
    Parametros:
        n: nº inteiro positivo
    Devolve:
        True se nº é primo 
        False se nº não é primo
    """
    #n_primo= True
    #for i in range(2,n):
    #    if n % 1 == 0:
    #        n_primo = False
    #        break
    #return n_primo

    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True