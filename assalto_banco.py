import math

def assalto():
    """
    Função que recebe o total de dinheiro conseguido no assalto
    """
    dinheiro= float(input("Insira o dinheiro roubado:"))
    return dinheiro

def partes(dinheiro):
    chefe= dinheiro / 2
    capangas = chefe / 2
    condutor = capangas / 2
    print(f"O chefe recebeu {chefe}€ os capangas receberam {capangas}€ e o condutor recebeu {condutor}€")
    return chefe, capangas,condutor

def duracao(dinheiro):
    """
    Função que recebe o dinheiro a gastar e calcular em quantos meses se gasta 
    """
    #calcular 5 do valor
    valor_mes= dinheiro * 0.05
    #verificar se utrapassa os 1000 €
    if valor_mes > 1000:
        valor_mes = 1000
    # calcular quantos meses dura
    meses= dinheiro / valor_mes
    meses= math.ceil(meses)
    print(f"Os {dinheiro}€ são gastos em {meses} meses, gastando {valor_mes}€ por mes") 

def main():
    dinheiro=assalto()
    partes(dinheiro)
    duracao(chefe)
    duracao(capangas)
    duracao(condutor)
    

if __name__ == "__main__":
    main()