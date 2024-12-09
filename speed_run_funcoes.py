#Afonso Costa n2
# Exercício de Funções em Python
# Complete cada função conforme indicado na docstring.
import math
import time
import datetime
def imprimir_dobro(valor):
    """Recebe um número e imprime o seu dobro."""
    dobro = valor * 2
    print(dobro)
	
def calcular_media_tres_numeros(n1, n2, n3):
    """
    Calcule a média aritmética de três números.
    Retorne o valor da média.
    """
    media= (n1 + n2 + n3) /3
    return media

def calcular_fatorial(numero):
    """Recebe um número inteiro positivo e retorna o seu fatorial.
	    Fatorial de 5 (5!) = 5 * 4 * 3 * 2 * 1
	"""
    fatorial = 0 
    for i in range (1,numero,+1):
        fatorial = fatorial * numero
    return fatorial
	
def converter_celsius_para_fahrenheit(celsius):
    """
    Converta a temperatura de Celsius para Fahrenheit.
    Fórmula: (°C × 9/5) + 32 = °F
    """
    fahrenheit= (celsius * 9/5) + 32
    return fahrenheit

def calcular_area_circulo(raio):
    """
    Calcule a área de um círculo dado o raio.
    Use pi = 3.14159
    """
    pi = 3,14159
    area= pi * raio **2
    return area

def exibir_contagem_regressiva(inicio):
    """Recebe um número e imprime uma contagem regressiva até 0."""
    for i in range(inicio,-1,-1):
        print(i)
    time.sleep(1)
#print(exibir_contagem_regressiva(10))

def inverter_string(texto):
    """
    Receba uma string e retorne ela invertida.
    Exemplo: "python" -> "nohtyp"
    """
    len(texto)
    texto_invertido= ""
    for i in range(len(texto) -1,-1,-1):
        texto_invertido = texto_invertido + texto[i]
    return texto_invertido
#print(inverter_string("python"))

def verificar_divisibilidade(a, b):
    """Recebe dois números e imprime se o primeiro é divisível pelo segundo."""
    if a % b == 0:
        print("Os numeros inseridos são divisiveis")
    else:
        print("Os numeros inseridos não são divisiveis")
#print(verificar_divisibilidade(10,2))

def calcular_perimetro_circulo(raio): 
    """Recebe o raio de um círculo e retorna o seu perímetro."""
    perimetro = 2 * math.pi * raio
    return perimetro
#print(calcular_perimetro_circulo(2))

def converter_segundos_para_minutos(segundos):
    """Recebe um valor em segundos e retorna o correspondente em minutos."""
    minutos= segundos // 60
    segundos_restam= segundos & 60 
    return f"{minutos}:{segundos_restam}"
#print(converter_segundos_para_minutos(60))

def gerar_saudacao_periodo():
    """
    Retorne uma saudação baseada no período do dia.
    Se for antes de 12h: "Bom dia!"
    Entre 12h e 18h: "Boa tarde!"
    Após 18h: "Boa noite!"
    """
    hora = datetime.datetime.now().hour
    if hora < 12:
        return "Bom dia"
    if hora > 12 and hora < 18:
        return "Boa tarde"
    if hora > 18:
        return "Boa noite"
#print(gerar_saudacao_periodo())

def calcular_desconto(preco, percentual):
    """Recebe um preço e um percentual de desconto e retorna o preço com desconto."""
    percentagem_pagar= 100 - percentual
    preco_com_desconto= preco * percentagem_pagar / 100
    return preco_com_desconto
#print(calcular_desconto(100,50))
    
def calcular_velocidade_media(distancia, tempo):
    """Recebe a distância percorrida e o tempo gasto e retorna a velocidade média."""
    pass

def verificar_palindromo(palavra):
    """
    Verifique se a palavra recebida é um palíndromo.
    Palíndromo é uma palavra que pode ser lida igual de trás para frente.
    Exemplo: "radar" é um palíndromo.
    """ 
    """
    len(palavra)
    frase_invertida= ""
    for i in range(len(palavra) -1,-1,-1):
        frase_invertida = frase_invertida + palavra[i]
    if frase_invertida == palavra:
        print(f"É palavra {palavra} é um palindromo")
    else:
        print(f"A palavra {palavra} não é um palindromo")
    """
    resultado= palavra == inverter_string(palavra)
    return resultado
print(verificar_palindromo("radar"))