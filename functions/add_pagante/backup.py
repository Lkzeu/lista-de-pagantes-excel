#!/usr/bin/env python3

from shutil import copy2
from os.path import exists, realpath, dirname
from os import getcwd, remove, name, system, listdir

def faz_backup(pasta_principal, arquivo_to_do_backup):
   # pasta_backup = realpath(getcwd()+'/backups/')
   pasta_backup = realpath(pasta_principal + '/backups/')
   # info_de_backup = realpath(getcwd()+'/functions/add_pagante/n_backup.dat') 
   info_de_backup = realpath(pasta_principal + '/functions/add_pagante/n_backup.dat')

   if exists(info_de_backup): 
      with open(info_de_backup) as read_backup:
         backups_existentes = ordena(listdir(pasta_backup))
         num_backups = read_backup.readline()   # primeira linha, referentes a quantos backups podem coexistir antes de sobrepor os antigos
         backups_feitos = read_backup.readline() # segunda linha informa quantos backups já foram feitos, a fim de incrementar tal número
         
         if len(backups_existentes) == int(num_backups):
            backup_name = ''.join(['backup ', str(backups_existentes[0]), '.xlsx'])   # resultado: 'backup 1.xlsx' por exemplo
            remover = realpath(pasta_backup + '/' + backup_name)
            remove(remover)

         _ = str(int(backups_feitos) + 1)
         f = ' '.join(['backup', _])
         destino = realpath(pasta_backup + "/" + f + ".xlsx")
         copy2(arquivo_to_do_backup, destino)

         with open(info_de_backup, 'w') as f:
            f.write(num_backups + _)  # num_backups e _ já têm o '\n' da gravação da linha 36
   else:
      system('cls' if name == 'nt' else 'clear') # limpa tela
      print("=-"*30)
      print("Vejo que é a primeira vez que executou o programa...\n"+"-"*60)
      print("Farei backup da sua planilha antes de fazer qualquer alteração")
      print("a fim de previnir a perda de todos os dados por causa de algum bug de execução...")
      print("=-"*30)
      print("\nQuantos backups você quer manter armazenados? (os mais antigos serão excluídos) ")
      numero_backups = quantos_backups("Digite a quantidade em número: ")

      with open(info_de_backup, 'w') as something:
         something.write(str(numero_backups) + '\n' + '0')

def quantos_backups(msg = ''):
   while True:
      x = int(input(msg))
      if x < 2 or x > 10:
         print("Você só pode ter no mínimo 2 e no máximo 10 backups.")
         continue
      return x

def ordena(iteravel):
   num_ordenado = []
   # separa 'backup n.xlsx' e cria uma lista apenas com 'n'
   for _ in iteravel:
      a, b = _.split()
      b = b[:-5]     # tira o '.xlsx' do nome
      num_ordenado.append(int(b))

   # ordena a lista apenas com 'n's
   for i in range(len(num_ordenado)):
      for j in range(len(num_ordenado) - 1):
         a, b = num_ordenado[j], num_ordenado[j + 1]
         if a > b:
            num_ordenado[j], num_ordenado[j + 1] = b, a
 
   return num_ordenado
