#!/usr/bin/env python3

from datetime import datetime

def coloca_zero(numero = 0):
   numero = '0' + str(numero) if numero < 10 else str(numero)
   return numero

def separa_dia_mes(data = '00/00/0000'):
   dia, mes, ano = data.split('/')
   return int(dia), int(mes), int(ano)

def dias_mes(mes = 1):
   meses = {
      'Janeiro' : 31,
      'Fevereiro' : 28,
      'Março' : 31,
      'Abril' : 30,
      'Maio' : 31,
      'Junho' : 30,
      'Julho' : 31,
      'Agosto' : 31,
      'Setembro' : 30,
      'Outubro' : 31,
      'Novembro' : 30,
      'Dezembro' : 31
   }
   mes = list(meses)[mes - 1]
   return meses[mes]

def vencimento(data = '00/00/0000', quantidade_de_mes = 1):
   dia, mes, ano = separa_dia_mes(data)
   dia += 31 * quantidade_de_mes
   
   while dia > dias_mes(mes):
      dia -= dias_mes(mes)
      mes += 1
      if mes > 12:
         ano += 1
         mes -= 12
   dia, mes = coloca_zero(dia), coloca_zero(mes)
   
   return '/'.join([dia, mes, str(ano)])

def pergunta(data, nome = ''):
   agora = datetime.now()
   dia, mes, ano = agora.day, agora.month, agora.year
   hoje = '/'.join([coloca_zero(dia), coloca_zero(mes), str(ano)])
   quantidade_mes = None

   if data == '':
      data = hoje
      quantidade_mes = 1
   else:
      data = input("Qual o dia de pagamento?")
      data = hoje if data == '' else data
      quantidade_mes = int(input("Quantos meses {nome} tem? "))

   return data, quantidade_mes