#Afonso Costa n2
def divisaR(preco,taxa):
        taxa= 4.05
        precoR = preco + taxa
        precoR = precoR + (10/100)
        return precoR

def divisaD(preco,taxa):
        taxa = 1.23
        precoD = preco + taxa
        precoD = precoD + (10/100)
        return precoD

def divisaL(preco,taxa):
        taxa = 0.89
        precoL = preco + taxa
        return precoL

def divisaT(preco,taxa):
        taxa = 4.67
        precoT = preco + taxa
        return precoT


def menu():
    taxas= input("Consultar taxas (S/N):")
    taxas = taxas.upper()
    if taxas == "S":
        print("R -> 4,05\nD -> 1,23\nL -> 0,89\nT -> 4,67")
    preco = float(input("Preço do produto (Euros):"))
    divisa = input("Divisa (R/D/L/T):")
    divisa = divisa.upper()
    if divisa == "R":
        print(divisaR(preco,divisa))
        divisaR(preco,divisa)
    if divisa == "D":
        divisaD(preco,divisa)
    if divisa == "L":
        divisaL(preco,divisa)
    if divisa == "T":
        divisaT(preco,divisa)

def main():
    menu()

if __name__ == "__main__":
    main()