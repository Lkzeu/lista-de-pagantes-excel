#!/usr/bin/env python3

from typing import Tuple

from functions.add_pagante import data

def get_vencimento(vencimentos, celula: int) -> str:
   vencimento_do_pagante = str(vencimentos[celula].value).strip()

   return vencimento_do_pagante

def dia_vencimento(vencimentos, celula: int) -> Tuple[int, int, int]:
   return data.separa_dia_mes(str(vencimentos[celula].value))
