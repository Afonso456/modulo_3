#Completa a função de acordo com a docstring
def RepetidasSeguidas(palavra):
    """
    Recebe uma string com um texto que deve ser verificado para encontrar letras seguidas iguais
    Parâmetro:
        texto: string a verificar
    Devolve:
        True: se o texto contém letras seguidas iguais
        False: se o texto não tem letras seguidas iguais
    """
    iguais=""
    for i in range(len(palavra)-1):
        iguais = palavra[i]
        palavra = palavra.lower()
        if iguais == palavra[i+1]:
            return True
    return False
        


#Testes
assert RepetidasSeguidas("Ana") == False, "Erro a função devia devolver False"
assert RepetidasSeguidas("Assar") == True, "Erro a função devia devolver True"
assert RepetidasSeguidas("") == False,"Erro a função devia devolver False"
assert RepetidasSeguidas("AsSado") == True, "Erro a função devia devolver False"

print("Função passou nos testes")