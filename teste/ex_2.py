def calcular_preco(preco,divisa):
    """
    Calcula o preço do produto
    """
    taxa=0
    taxa_alfandega= 0
    if divisa == "r":
        taxa = 4.05
        taxa_alfandega= 0.1
    if divisa == "d":
        taxa = 1.23
        taxa_alfandega = 0.1
    if divisa == "l":
        taxa= 0.89
    if divisa == "t":
        taxa= 4.67
    
    preco_convertido= preco * taxa
    preco_convertido = preco_convertido + (preco_convertido * taxa_alfandega)
    return (preco_convertido,2)

def nome_divisa(divisa):
    """
    Mostra o nome das divisas por extenso
    """
    texto= ""
    if divisa == "r":
        print("Reais [Brail]")
    if divisa == "d":
        print("Dolares [EUA]")
    if divisa == "l":
        print("Libras Esterlinas [UK]")
    else:
        print("")

def mostrar_taxas():
    """
    Mostra as taxas de conversão
    """
    print("Taxas:\nR -> 4,05\nD -> 1,23\nL -> 0,89\nT -> 4,67")

def main():
    op = input("Consultar taxas (s/n):")
    preco= float(input("Preço do produto:"))
    if preco <= 0:
        print("O valor tem de ser positivio")
    divisa=input("Divisa (R/D/L/T):")
    if divisa not in "rdlt":
        print("A dvisa tem que ser (R/D/L/T)")
    if op == "s":
        mostrar_taxas()

if __name__ == "__main__":
    main()