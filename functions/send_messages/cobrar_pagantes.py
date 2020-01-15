#!/usr/bin/env python3

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

from functions.send_messages.numbers_excel_2_txt import numbers_xl_to_txt

import os
import time
import pyperclip

def enviar(arquivo = '', mes = ''):  
   cobrar_numeros, cobrar_vencimento = numbers_xl_to_txt(arquivo, mes) # Esta função retorna duas strings com os nomes dos txts dos numeros e vencimentos, respectivamente
   
   msg1, msg2 = "(Mensagem automática). Seu vencimento é dia ", ". Você tem até 1 dia após o vencimento para me enviar o comprovante, ou seu acesso será revogado."

   chrome = "chromedriver.exe" if os.name == 'nt' else "chromedriver"  # se for windows coloca o '.exe' ao final do arquivo
   chromedriver = os.path.realpath('/'.join([os.getcwd(), 'functions/send_messages', chrome])) # /caminho/ate/chromedriver.exe/
   driver = webdriver.Chrome(chromedriver)
   driver.get("https://web.whatsapp.com")
   time.sleep(20)

   with open(cobrar_numeros) as number:
      i = 1
      x = open(cobrar_vencimento)
      for _ in number:
         _ = _.rstrip()
         venc = x.readline()
         link = "https://web.whatsapp.com/send?phone="+_+"&amp;source=&amp;data="
         msg_completa = msg1 + venc + msg2
         pyperclip.copy(msg_completa)
         
         driver.get(link)
         time.sleep(10)

         num_de_tentativas = 1
         controle = None
         while controle == None:
            try:
               input_box = driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]') 
               input_box.send_keys(Keys.CONTROL+"v")
               time.sleep(2)
               input_box.send_keys(Keys.ENTER)
               time.sleep(10)

               controle = 1

            # caso não consiga enviar a mensagem armazena o número do contato falho
            # em um log de falhas
            except NoSuchElementException:
               if num_de_tentativas > 3:
                  with open("log de falha.txt", 'a+') as fail:
                     fail.write(_+'\n')
                     break
               controle = None
               time.sleep(2)
               fail += 1 
         i += 1
      x.close()

   # remove os arquivos
   os.remove(cobrar_numeros)
   os.remove(cobrar_vencimento)
# fim 