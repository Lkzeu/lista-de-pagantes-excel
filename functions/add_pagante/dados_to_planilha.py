#!/usr/bin/env python3

from openpyxl.styles import Font, Alignment
#from openpyxl import Workbook, load_workbook

def insert_dados(line, ws, dado, alinhamento, fonte = Font(name='Arial', size=10)):
   coluna = 1  # valor constante, para começar a inserir sempre a partir da coluna A
   alinha = [] 
   
   # cria as funções de alinhamento, substituindo '_' por 'center' por exemplo
   for _ in alinhamento:
      alinha.append(Alignment(horizontal = _))

   # insere os dados na planilha
   for _ in range(5):
      escreve = ws.cell(row=line, column=(coluna + _))
      escreve.value = dado[_]
      escreve.font, escreve.alignment = fonte, alinha[_]