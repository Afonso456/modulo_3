"""
Programa para calcular o vencimento de um trabalhador.
O programa deve começar por solicitar ao trabalhador que indique o seu nome, quantas horas trabalhou por dia, e quanto ganha 
por hora. Caso o trabalhador tenho mais do que 8 horas de trabalho deve receber, por cada hora extra recebe mais 25%. 
Caso tenha trabalhado mais do que 10 horas por dia deve receber 50% por cada hora além das 10 horas.
"""

def PedirNomeTrabalhador(nome:str):
    """Esta função deve pedir o nome do trabalhador. O nome deve ter pelo menos 3 letras."""
    tamanho= len[nome]
    if tamanho == 8:
        PedirNomeTrabalhador()
    else:
        print("Insira um nome maior")

def PedirHorasTrabalho(horas_trabalho):
    """Esta função pede ao utilizador quantas horas trabalho no dia. O nº de horas deve ser superior a zero."""
    if horas_trabalho < 0:
        print("Insira um numero dse horas valido")
        PedirHorasTrabalho()


def PedirOrdenado(ordenado):
    """Esta função pede ao utilizado quanto ganha por cada hora de trabalho"""
    if ordenado < 0:
        print("Insira um valor valido")
        PedirOrdenado()

def MostrarVencimento(nome,horas,ordenado_por_hora):
    """Esta função deve mostrar o nome do trabalhador e quanto é que deve receber pelo dia de trabalho"""
    if len[nome] < 3:
        print("Insira um nome maior")
    ordenado= PedirOrdenado(ordenado)
    ordenado_por_hora= horas * ordenado
    if horas > 8:
        ordenado_por_hora= ordenado + 0.25
    elif horas > 10:
        ordenado_por_hora= ordenado + 0.5
        return ordenado_por_hora
    pass

def main():
    # Função principal do programa

    # pedir o nome do trabalhador
    nome= input("Insira o seu nome:")
    PedirNomeTrabalhador(nome)
    # pedir as horas que trabalhou
    horas_trabalho= input("Insira as horas de trabalho:")
    PedirHorasTrabalho(horas_trabalho)
    # pedir o ordenado por hora
    ordenado= input("Insira o seu ordenado:")
    PedirOrdenado(ordenado)
    # calcular e mostrar o vencimento~
    pass
if __name__=="__main__":
    main()