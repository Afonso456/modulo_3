"""
Programa para implementar um acalculadora simples utilizando funções
"""
def somar(x,y):
    """Função que recebe dois numeros e mostrar a sua soma"""
    print(x+y)
def subtrair(x,y):
    """Função que recebe dois numeros e mostrar a diferença"""
    print(x-y)
def multiplicar(x,y):
    """Função que recebe dois numeros e mostrar o produto"""
    print(x*y)
def divisao(x,y):
    """Função que recebe dois numero e mostrar a divisão """
    print(x/y)

def menu():
    """
    Mostra ao utilizador as operações que a calculadora vai realizar
    """
    op = 0
    while op != 5:
        print("1.Soma\n2.Subtração\n3.Multiplicar\n4.Dividir\n5.Terminar")
        op=input()
        if op == "5":
            break
        x= float(input("Insira um nº:"))
        y= float(input("Insira um nº:"))
        if op == "1":
            somar(x,y)
        elif op == "2":
            subtrair(x,y)
        elif op == "3":
            multiplicar(x,y)
        elif op == "4":
            divisao(x,y)

def main():
    menu()

if __name__ == "__main__":
    main()
