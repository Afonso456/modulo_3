#Afonso Costa n2
def n_perfeito(numero):
    soma= 0
    for i in range(1,numero):
        if numero % i == 0 and numero > 0:
            soma += i
    if numero == soma:
        return True
    return False
            
def main():
    numero= int(input("Insira um numero:"))
    if n_perfeito(numero) == True:
        print("Numero perfeito")
    else:
        print("Numero não perfeito")
    
if __name__ == "__main__":
    main()