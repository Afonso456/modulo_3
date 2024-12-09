"""
Dois numeros primos gémeos são dois nºs primos que distam em 2 unidades um do outro
EX:
    3 e 5 
    5 e 7 
Fazer um programa que lê do utilizador 2 nºs inteiros positivos e diz se são primos e primos gémeos
"""
import primo
from utils import n_inteiro
n1= n_inteiro("Insira um nº:")
n2= n_inteiro("Insira um nº:")
if primo.primo(n1) and primo.primo(n2):
    diferenca = n1 - n2
    if abs(diferenca) == 2:
        print(f"O valores {n1} e {n2} são primos gêmeos")
    else:
        print(f"O valores {n1} e {n2} são primos")
else:
    if primo.primo(n1):
        print(f"O número {n1} é primo")
    elif primo.primo(n2):
        print(f"O número {n2} é primo")
    else:
        print("Nenhum deles é primo")