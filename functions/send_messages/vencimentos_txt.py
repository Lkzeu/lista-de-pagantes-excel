#!/usr/bin/env python3

from functions.add_pagante import data

def venc_em_txt(wb, ws, celula, vencimento_txt):
   vencimentos = ws['E']
   vencimento_do_pagante = str(vencimentos[celula].value)
   with open(vencimento_txt, 'a+') as f:
      f.write(vencimento_do_pagante + '\n')

def dia_vencimento(wb, ws, celula):
   vencimentos = ws['E']
   return data.separa_dia_mes(str(vencimentos[celula].value))