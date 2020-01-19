#!/usr/bin/env python3

import os
import time

import pyperclip
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

from functions.send_messages.numbers_excel_2_txt import numbers_xl_to_txt

def enviar(pasta_principal, arquivo, mes):
   numeros_e_vencimentos = numbers_xl_to_txt(arquivo, mes)
   msg1 = "(Mensagem automática). Seu vencimento é dia ",
   msg2 = ". Você tem até 1 dia após o vencimento para me enviar o comprovante, ou seu acesso será revogado."

   chrome = "chromedriver.exe" if os.name == 'nt' else "chromedriver"
   chromedriver = os.path.realpath(pasta_principal + '/functions/send_messages/' + chrome)
   driver = webdriver.Chrome(chromedriver)
   driver.get("https://web.whatsapp.com")
   time.sleep(20)

   for numero, vencimento in numeros_e_vencimentos.items():
      link = "https://web.whatsapp.com/send?phone=" + numero + "&amp;source=&amp;data="
      msg_completa = msg1 + vencimento + msg2
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

         except NoSuchElementException:
            if num_de_tentativas > 3:
               with open("log de falha.txt", 'a+') as fail:
                  error_message = (f'Numero: {numero}\n'
                  f'Vencimento: {vencimento}\n'
                  'ERROR: could not send the message. '
                  "The number doesn't exist or it's incorrect\n")

                  fail.write(error_message)
            else:
               controle = None
               time.sleep(2)
