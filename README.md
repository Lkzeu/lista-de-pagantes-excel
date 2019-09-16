# Lista de Pagantes Excel
Um projeto em python onde pude aplicar meus conhecimentos para adicionar dados de pagantes a uma planilha Excel e enviar mensagens automatizadas com o dia de vencimento de cada pagante através do Whatsapp.

### Por quê?
Eu tinha a necessidade de automatizar a inserção de novos pagantes a uma planilha em excel e de cobrar, pelo whatsapp, várias pessoas em dias variados.
### Requísitos
- [Python 3](https://www.python.org/)

- __Selenium__ </br>
  >Windows: pip install selenium </br>
  >Linux: pip3 install selenium </br>
- __Openpyxl__ </br>
  >Windows: pip install openpyxl </br>
  >Linux: pip3 install openpyxl </br>
- __Pyperclip__ </br>
  >Windows: pip install pyperclip </br>
  >Linux: pip3 install pyperclip </br>
### Funções
- [x] Detecta automáticamente o mês e adiciona todos os dados na folha correspondente ao mês
- [x] Se não existir uma folha com o mês corrente, esta é criada automaticamente
