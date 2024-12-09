original= "abcdefghijklmnopqrstuvwxyz"
codigo=   "bcdefghijklmnopqrstuvwxyza"

def menu(op):
    """Função que lê a opção do utilizador: codificar ou descodificar"""
    print(op=input("Deseja codificar ou descodificar:"))
    if op == "codificar":
        print(codificada("ola mundo"))
    if op == "descodificar":    
        print(descodifica("pmbnvoep"))
    
def codificada(mensagem:str)->str:
    """Função que recebe uma mensagem e devolve a mesma codificada de acordo com os alfabetos fornecidos"""
    global original
    global codigo
    texto=""
    for l in mensagem:
        #caso não encontre a letra no alfabeto deve manter a letra original
        if l not in original:
            texto = texto + l    
        else:    
            for p in range (len(original)):
                if l == original[p]:
                    texto = texto + codigo[p]
        
    return texto
        
def descodifica(mensagem_codificada:str)->str:
    """Função que recebe uma mensagem e devolve a mesma descodificada de acordo com os alfabetos fornecidos"""
    global original
    global codigo
    texto=""
    for l in mensagem_codificada:
        #caso não encontre a letra no alfabeto deve manter a letra original
        if l not in codigo:
            texto = texto + l    
        else:    
            for p in range (len(codigo)):
                if l == codigo[p]:
                    texto = texto + original[p]
    return texto    
                                  
def main():
    print(menu())

if __name__ == "__main__":
    main()