#!/usr/bin/env python3

from datetime import datetime
from openpyxl import load_workbook

from functions.send_messages.vencimentos_txt import venc_em_txt, dia_vencimento
from functions.send_messages.verifica_se_eh_brazileiro import is_brazil

# pega cada número da planilha e add a um txt
def numbers_xl_to_txt(arquivo = '', mes = ''): 
   txt_numeros = 'TXTs/tmp_cobrar numeros.txt'
   txt_vencimentos = 'TXTs/tmp_vencimentos.txt'
   wb = load_workbook(arquivo)
   ws = wb[mes]
   n_pagantes = ws['B']
   
   agora = datetime.now()
   hoje = agora.day

   # cria dois intervalos; ]0, 15], ]15, 31]
   # em cada intervalo são enviadas mensagens para as pessoas
   # que os dias de seus vencimentos se enquadram no intervalo 
   if hoje < 15:
      min, max = 0, 15 
   else:
      min, max = 15, 31

   for celula in range(1, ws.max_row):
      numero = str(n_pagantes[celula].value)    # pega o número da pessoa
      dia, month, ano = dia_vencimento(wb, wb[mes], celula)  # retorna o dia e mes do vencimento da pessoa
      if min < dia <= max and month == agora.month and ano == agora.year:  # verifica se seu vencimento está no intervalo
         salva(numero, txt_numeros)       # cria um txt com os numeros
         venc_em_txt(wb, wb[mes], celula, txt_vencimentos) # cria um txt com os vencimentos    

   return txt_numeros, txt_vencimentos

# salva o número em um txt, diferenciando números brasileiros de estrangeiros
def salva(number, txt):
   with open(txt, 'a+') as num:
      if is_brazil(str(number)):
         num.write("55"+number+'\n')
      else:
         num.write(number+'\n')
