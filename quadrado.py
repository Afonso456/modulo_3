def quadrado_inteiro(n):
    """Função que pede ao utilizador e devolve o seu quadrado inteiro"""
    n_quadrado= n **2
    return n_quadrado
def main():
    n= int(input("Insira um numero:"))
    q= quadrado_inteiro(n)
    print(f"O quadrado de {n} é {q}")
    
if __name__ == "__main__":
    main()