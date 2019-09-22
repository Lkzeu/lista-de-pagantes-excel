# Lista de Pagantes Excel
Um projeto em python onde pude aplicar meus conhecimentos para adicionar dados de assinantes a uma planilha Excel e enviar mensagens automatizadas com o dia de vencimento de cada assinantes através do Whatsapp.

### Por quê?
Eu tinha a necessidade de automatizar a inserção de novos assinantes a uma planilha em excel e de cobrar, pelo whatsapp, várias pessoas em dias variados.
### Requísitos
- [Python 3](https://www.python.org/)  

- [Chromedriver](https://chromedriver.chromium.org/downloads)  
  >__Deve__ estar solto junto com o arquivo "main.py" e "add_pagantes.py"  

- __Selenium__
  >Windows: pip install selenium  
  >Linux: pip3 install selenium  
- __Openpyxl__  
  >Windows: pip install openpyxl  
  >Linux: pip3 install openpyxl  
- __Pyperclip__  
  >Windows: pip install pyperclip  
  >Linux: pip3 install pyperclip  

### Funções
- [x] Detecta automáticamente o mês e adiciona todos os dados na folha correspondente ao mês;  
- [x] Se não existir uma folha com o mês corrente, esta é criada automaticamente;  
- [x] Backup da planilha antes de qualquer alteração;  
- [x] Não lota o HD de backups, pois mantém o número de backups desejado, excluindo os mais antigos;  
- [x] Vencimento automático com padrão de 1 mês a partir da data de pagamento;
- [x] Opção de inserção de data de pagamento Manual ou Automática (dia de hoje);
- [x] Possibilidade de mudar o padrão de meses para o vencimento.