#!/usr/bin/env python3

from datetime import datetime
from os.path import realpath, dirname, exists
from os import mkdir

from functions.send_messages import cobrar_pagantes
from functions.add_pagante import add_pagantes
from functions.send_messages import numbers_excel_2_txt

def main(pasta_principal):
   now = datetime.now()
   meses = ["Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho",
            "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"]
   mes = meses[now.month - 1]

   planilha = '/planilha/pagantes '

   while True:
      x = int(input("1 - adicionar pessoas\n"
                    "2 - enviar mensagens\n"))

      if x == 1:
         arquivo = realpath(pasta_principal + planilha + str(now.year) + '.xlsx')
         add_pagantes.cria_pagantes(pasta_principal, arquivo, mes)
      elif x == 2:
         year = now.year
         mes = now.month
         if now.month == 1:
            year -= 1
            mes = 13
         arquivo = realpath(pasta_principal + planilha + str(year) + '.xlsx')
         cobrar_pagantes.enviar(pasta_principal, arquivo, meses[mes - 2])
      else:
         print("opção inválida!")
         continue
      break

def cria_pasta(caminho):
   if not exists(caminho):
      mkdir(caminho)

if __name__ == '__main__':
   pasta_principal = dirname(realpath(__file__))
   pasta_backup = realpath(pasta_principal + '/backups/')
   pasta_planilha = realpath(pasta_principal + '/planilha/')

   cria_pasta(pasta_backup)
   cria_pasta(pasta_planilha)

   main(pasta_principal)
