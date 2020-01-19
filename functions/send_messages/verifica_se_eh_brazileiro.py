#!/usr/bin/env python3

def is_brasileiro(telefone: str) -> bool:
   # se o número passar em um dos testes será verificado o DDD, caso seja um DDD brasileiro
   # retornará a condição para acrescentar o '55' ao numero na função get_numero_formatado()
   if len(telefone) == 10 or (len(telefone) == 11 and telefone[2] == '9'):
      ddds = open("TXTs/ddd.txt", encoding = 'utf-8').read()
      return True if telefone[0:2] in ddds else False
   return False
