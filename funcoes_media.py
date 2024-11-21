#Programa que le 3 nº calcula e mostra a media
def mediaA():
    x= int(input("X:"))
    y= int(input("Y:"))
    z= int(input("Z:"))
    m= (x + y + z) / 3
    print(f"A media é de {m}")

#Programa que recebe 3 nºs e calcula e mostra a media
def mediaB(x,y,z):
    m= (x + y + z) / 3
    print(m)

#Programa que lê 3 nºs e calcula e devolve a media
def mediaC():
    x= int(input("X:"))
    y= int(input("Y:"))
    z= int(input("Y:"))
    m= (x+y+z) /3
    return m

#Programa que recebe 3 nºs calcula e devolve a media 
def mediaD(x,y,z):
    m= (x+y+z) /3
    return m

def main():
    mediaA()
    mediaB(5,5,5)
    print(mediaC()) #chama a função e mostra o valor devolvido
    print(f"A media é de {mediaD(5,5,5)}") #chama a função com os argumentos e mostra o valor devolvido

if __name__ == "__main__":
    main()