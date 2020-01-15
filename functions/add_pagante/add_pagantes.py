#!/usr/bin/env python3

from shutil import copy2

import os

from functions.add_pagante import data
from functions.add_pagante import backup
from functions.add_pagante import dados_to_planilha
from functions.add_pagante import verificar_planilha

def cria_pagantes(pasta_principal, planilha = '', mes = ''):
   wb, ws = verificar_planilha.abrir_planilha(planilha, mes)
   backup.faz_backup(pasta_principal, planilha)
   
   line = ws.max_row + 1   
   dados_da_pessoa = None 
   meses_para_vencimento = None 

   x = None
   dados = ('nome', 'numero', 'email', 'dia de pagamento')  
   while True:
      os.system('cls' if os.name == 'nt' else 'clear') # limpa tela
      print("-"*40+"\nDados da {}ª pessoa!".format(line - 1))
      print("crtl + c para finalizar o programa!\n"+"-"*40)
      print("obs.: Dia de pagamento; aparte Enter para hoje ou 'S' para 2 meses ou +\n\n")   

      dados_da_pessoa = [] # sempre que os dados estivem incorretos a lista é zerada
      meses_para_vencimento = 1 # "" o padrão é reestabelicido para 1

      try:
         # pega todos os dados das pessoas e armazena em uma lista vazia
         for _ in dados:
            x = input("Digite o {} da pessoa: ".format(_))

            if x == '' or x.lower() == 's':
               x, meses_para_vencimento = data.pergunta(x, dados_da_pessoa[0])
            dados_da_pessoa.append(x)
                
      except KeyboardInterrupt:
         print("\nPrograma finalizado!\n")
         wb.save(planilha)
         raise SystemExit(0) # mesmo que sys.exit()

      # caso tenha errado em algum dado, poderá inseri-los
      # novamente antes de colocá-los diretamente na planilha
      confirma = input("Todos os dados estão certos? [s/n] ").lower()
      if confirma == 'nao' or confirma == 'n':
         continue
         
      dia_de_vencimento = data.vencimento(dados_da_pessoa[3], meses_para_vencimento)  # index 3 é o dia do pagamento.
      dados_da_pessoa.append(dia_de_vencimento)
            
      # os dados são inseridos na planilha
      alinha = ('center', 'center', 'left', 'right', 'right')
      dados_to_planilha.insert_dados(line, ws, dados_da_pessoa, alinha)
      line += 1
