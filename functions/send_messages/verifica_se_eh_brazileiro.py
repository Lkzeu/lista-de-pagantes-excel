#!/usr/bin/env python3

# verifica se um número é brasileiro ou não
def is_brazil(telefone = ''):
   # se o número passar em um dos testes será verificado o DDD, caso seja um DDD brasileiro
   # retornará a condição para ser gravado como número brasileiro no TXT da função 'salva()'
   if len(telefone) == 10 or (len(telefone) == 11 and telefone[2] == '9'):
      with open("TXTs/ddd.txt") as a:
         ddds = a.read()
         return True if telefone[0:2] in ddds else False
   return False