#!/usr/bin/env python3

from datetime import datetime
from os.path import realpath
from os import getcwd
import os

from functions.send_messages import cobrar_pagantes
from functions.add_pagante import add_pagantes
from functions.send_messages import numbers_excel_2_txt

def main(pasta_principal):
   now = datetime.now()
   meses = ["Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho",
            "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"]         
   mes = meses[now.month - 1]
   nome_planilha = '/planilha/pagantes ' + str(now.year) + '.xlsx'
   # arquivo = realpath(getcwd() + nome_planilha)
   
   arquivo = realpath(pasta_principal + nome_planilha) 

   while True:
      x = int(input("1 - adicionar pessoas\n"
                    "2 - enviar mensagens\n"))

      if x == 1:
         add_pagantes.cria_pagantes(pasta_principal, arquivo, mes)
      elif x == 2:
         cobrar_pagantes.enviar(arquivo, meses[now.month - 2])
      else:
         print("opção inválida!")
         continue
      break

def cria_pasta(caminho):
   if os.path.exists(caminho):
      pass
   else:
      os.mkdir(caminho)
if __name__ == '__main__':
   pasta_principal = os.path.dirname(realpath(__file__))
   pasta_backup = realpath(pasta_principal + '/backups/')
   pasta_planilha = realpath(pasta_principal + '/planilha/')

   cria_pasta(pasta_backup)
   cria_pasta(pasta_planilha)

   main(pasta_principal)
