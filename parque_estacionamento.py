from datetime import datetime
def duracao_estacionamento(hora:int,minutos:int):
    """Função que recebe o tempo de estacionamento"""
    hora_atual= datetime.now().hour
    minutos_atuais= datetime.now().minute
    n_horas = hora_atual - hora
    n_minutos = minutos_atuais - minutos
    if minutos < 0:
        n_horas -= 1
        n_minutos = 60 - minutos + minutos_atuais
    duracao_total_minutos= n_horas * 60 + n_minutos 
    return duracao_total_minutos
def blocos_minutos(minutos:int):
    """Função que recebe a duração em minutos e devolve quantos blocos de 15 min existem """
    n_blocos = minutos // 15
    if minutos % 15 != 0:
        n_blocos += 1
    return n_blocos

def Custo(blocos:int, preco_bloco:float)-> float:
    """
    Função que calcula o custo do estacionamento com base na duração em blocos de 15 min e o preço de cada bloco"""
    return blocos * preco_bloco

def main():
    preco= float(input("Preço por cada 15 minutos:"))
    horas= int(input("Horas:"))
    minutos= int(input("Minutos:"))
    duracao_minutos= duracao_estacionamento(horas,minutos)
    blocos= blocos_minutos(duracao_minutos)
    custo = Custo(blocos,preco)
    print(f"Estacionameto com duração de {duracao_minutos} minutos que corresponde a {blocos} blocos de 15 minutos com o custo de {custo}€")

if __name__ == "__main__":
    main()