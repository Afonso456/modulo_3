import utils
def menu():
    """
    Função que cria um menu 
    """
    op= 1
    while op != 4:
        op= utils.minimo_maximo_inteiro(1,4,"1.Entrada \n2.Saida \n3.Estado \n4.Terminar \n")
        if op == 1:
            entrada_clientes()
            entrada_mesas()
            
        if op == 2:
            saida_clientes()
            saida_mesas()

        if op == 3:
            estado()

def entrada_clientes():
    """
    Responsavel por registar a entrada dos clientes
    """
    global n_max_clientes
    global n_atual_clientes
    #testar se o restaurante não pode receber mais clientes
    if n_atual_clientes == n_max_clientes:
        return 0
    #ler o numero de clientes a entrar
    lugares_livres= n_max_clientes - n_atual_clientes
    entrar= utils.minimo_maximo_inteiro(1, lugares_livres, "Quantos clientes são:")
    n_atual_clientes += entrar 
    
def entrada_mesas():
    """
    Responsavel por registar a ocupação das mesas
    """
    global n_max_mesas
    global n_atual_mesas
    if n_max_mesas == n_atual_mesas:
        print("O restaurante está cheio")
        return 0
    mesas_livres= n_max_mesas - n_atual_mesas
    entrar= utils.minimo_maximo_inteiro(1,mesas_livres, "Quantas mesas:")
    n_atual_mesas += entrar 

def estado():
    """
    Função que calcula e mostra os dados estatisticos   
    """
    global n_max_mesas
    global n_max_clientes
    n_max_mesas -= n_atual_mesas
    n_max_clientes -= n_atual_clientes
    print(f"Estão ocupadas {n_atual_mesas} mesas e estão {n_atual_clientes} clientes")
    print(f"Ainda possui {n_max_mesas} mesas e {n_max_clientes} lugares")
    print(f"Já recebeu {total_pago} das refeições servidas")

def saida_clientes():
    """
    Responsavel por registar a saida dos clientes
    """
    global n_atual_clientes
    global total_pago
    if n_atual_clientes == 0:
        print("Não tem clientes")
        return 0
    n_clientes= utils.minimo_maximo_inteiro(1,n_atual_clientes, "Quantos clientes saiem do restaurante:")
    n_atual_clientes += n_clientes
    pagou= utils.minimo_maximo_inteiro(0,None,"Quanto custou a refeição:")
    total_pago = total_pago + pagou

def saida_mesas():
    """
    Responsavel por registar as mesas desocupadas
    """
    global n_atual_mesas
    if n_atual_mesas == 0:
        print("Não tem clientes")
        return 0
    n_mesas= utils.minimo_maximo_inteiro(1,n_atual_mesas, "Quantas mesas ficam desocupadas:")
    n_atual_mesas += n_mesas

n_max_mesas= utils.n_inteiro("Quantas mesas tem o restaurante:")
n_max_clientes= utils.n_inteiro("Qual o maximo de clientes que podem estar no restaurante:")
n_atual_mesas= 0
n_atual_clientes= 0
total_pago= 0

def main():
    menu()
if __name__ == "__main__":
    main()