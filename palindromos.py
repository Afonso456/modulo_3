def palindromo(palavra): 
    """
    Função que recebe uma string e indica se é um palindromo ou não
    Parametros: 
        palavra: string a testar
    Devolve:
        True se for palindromo
        False se não for palindromo
    """
    frase_invertida= ""
    palavra= input("Insira uma palavra:")
    for posicao in range(len(palavra) -1,-1,-1):
        frase_invertida = frase_invertida + palavra[posicao]
    if frase_invertida == palavra:
        return True
    return False

def main():
    palavra= input("Insira uma palavra:")
    if palindromo(palavra) == True:
        print(f"{palavra} é um palindromo")
    else:
        print(f"{palavra} não é um palindromo")
        
if __name__ =="__main__":
    main()