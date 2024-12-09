import sys
import os
import math
import datetime

#Modulo sys
print(len(sys.argv))

for arg in sys.argv:
    print(arg)

#Modulo os
print(os.name)
print(os.getcwd())

#Modulo math 
x= 9
print(math.sqrt(x))  #raiz quadrada
print(math.pow(3,2)) #exponenciação
print(3 ** 2)        #exponenciação
x= 0.3 * 3 
print(x == 0.9)
print(math.isclose(x,0.9))
print(abs(-5))       #valores inteiros
print(math.fabs(-5)) #floats

#Modulo date time

#data de hoje
print(datetime.date.today())

#ano
print(datetime.date.today().year)
#mes
print(datetime.date.today().month)
#dia
print(datetime.date.today().day)

#data e hora
print(datetime.datetime.now().hour)

#formatar para string e deixar apenas uma parte da data e do tempo
print(datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S"))