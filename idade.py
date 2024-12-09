#calcular a idade em anos
import datetime
dia= int(input("Dia de nacimento:"))
mes= int(input("Mes de nascimento:"))
ano= int(input("Ano de nascimento:"))
#data atual
hoje= datetime.date.today()

#objeto com data denascimento
data_nascimento= datetime.date(ano,mes,dia)

#calcular a idade
idade= hoje.year - data_nascimento.year
#verificar se ainda n fez anos este ano 
if data_nascimento.month > hoje.month or (data_nascimento.month == hoje.month and data_nascimento.day > hoje.day):
    idade -= 1
print(idade)

#powercfg/batteryreport/output"C:\battery_report.html"