#Programa que lê 3 notas e calcula a media
import funcoes_media
from funcoes_media import mediaD
nota1= int(input("Insira uma nota:"))
nota2= int(input("Insira uma nota:"))
nota3= int(input("Insira uma nota:"))
media= funcoes_media.mediaD(nota1,nota2,nota3)
print(f"A media é de {media}")