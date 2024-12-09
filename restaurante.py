import utils
def menu():
    """
    Função que cria um menu 
    """
    n_max_mesas= utils.n_inteiro("Quantas mesas tem o restaurante:")
    n_max_clientes= utils.n_inteiro("Qual o maximo de clientes que podem estar no restaurante:")
    op= 1
    n_atual_mesas= 0
    n_atual_clientes= 0
    total_pago= 0
    while op != 4:
        op= utils.minimo_maximo_inteiro(1,4,"1.Entrada \n2.Saida \n3.Estado \n4.Terminar \n")
        if op == 1:
            clientes_entrar= entrada_clientes(n_max_clientes,n_atual_clientes)
            mesas_ocupar= entrada_mesas(n_max_mesas,n_atual_mesas)
            n_atual_clientes += clientes_entrar
            n_atual_mesas += mesas_ocupar
        if op == 2:
            n_clientes_sairam= saida_clientes(n_atual_clientes)
            n_mesas_desocupadas= saida_mesas(n_atual_mesas)
            n_atual_clientes = n_atual_clientes- n_clientes_sairam
            n_atual_mesas = n_atual_mesas - n_mesas_desocupadas
            if n_clientes_sairam > 0 or n_mesas_desocupadas > 0:
                pagou= utils.minimo_maximo_inteiro(0,None,"Quanto custou a refeição:")
                total_pago = total_pago + pagou
        if op == 3:
            estado(n_max_mesas,n_max_clientes,n_atual_mesas,n_atual_clientes,total_pago)

def entrada_clientes(n_max_clientes,n_atual_clientes):
    """
    Responsavel por registar a entrada dos clientes
    """
    #testar se o restaurante não pode receber mais clientes
    if n_atual_clientes == n_max_clientes:
        return 0
    #ler o numero de clientes a entrar
    lugares_livres= n_max_clientes - n_atual_clientes
    entrar= utils.minimo_maximo_inteiro(1, lugares_livres, "Quantos clientes são:")
    #devolve o numero de 
    return entrar

def entrada_mesas(max_mesas,n_atual):
    """
    Responsavel por registar a ocupação das mesas
    """
    if max_mesas == n_atual:
        print("O restaurante está cheio")
        return 0
    mesas_livres= max_mesas - n_atual
    entrar= utils.minimo_maximo_inteiro(1,mesas_livres, "Quantas mesas:")
    return entrar

def estado(max_mesas,max_clientes,atual_mesas,atual_clientes,total):
    """
    Função que calcula e mostra os dados estatisticos   
    """
    max_mesas -= atual_mesas
    max_clientes -= atual_clientes
    print(f"Estão ocupadas {atual_mesas} mesas e estão {atual_clientes} clientes")
    print(f"Ainda possui {max_mesas} mesas e {max_clientes} lugares")
    print(f"Já recebeu {total} das refeições servidas")

def saida_clientes(n_atual_clientes):
    """
    Responsavel por registar a saida dos clientes
    """
    if n_atual_clientes == 0:
        print("Não tem clientes")
        return 0
    n_clientes= utils.minimo_maximo_inteiro(1,n_atual_clientes, "Quantos clientes saiem do restaurante:")
    return n_clientes

def saida_mesas(n_atual_mesas):
    """
    Responsavel por registar as mesas desocupadas
    """
    if n_atual_mesas == 0:
        print("Não tem clientes")
        return 0
    n_mesas= utils.minimo_maximo_inteiro(1,n_atual_mesas, "Quantas mesas ficam desocupadas:")
    return n_mesas

def main():
    menu()
if __name__ == "__main__":
    main()