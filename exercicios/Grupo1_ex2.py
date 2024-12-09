"""
Função que lê os valores do utilizador e clacula e mostra a media entre eles
"""
def Media():
    n1=int(input("Insira um nº"))
    n2=int(input("Insira um nº"))
    n3=int(input("Insira um nº"))
    n4=int(input("Insira um nº"))
    n5=int(input("Insira um nº"))
    soma= n1 + n2 + n3 + n4 + n5
    media= soma / 5
    print(media)

def Media_v2():
    soma= 0
    for _ in range(5):
        n= int(input("Insira um nº"))
        soma = soma + n
    media= soma / 5
    print(media)

Media()
Media_v2()