# Lista de Pagantes Excel
Um projeto em python onde pude aplicar meus conhecimentos para adicionar dados de assinantes a uma planilha Excel e enviar mensagens automatizadas com o dia de vencimento de cada assinantes através do Whatsapp.

### Por quê?
Eu tinha a necessidade de automatizar a inserção de novos assinantes a uma planilha em excel e de cobrar, pelo whatsapp, várias pessoas em dias variados.
### Requisitos
- Ter o [Chromedriver](https://chromedriver.chromium.org/downloads) instalado. O mesmo deve estar dentro da pasta "functions/send_messages"

### Funções
- [x] Detecta automáticamente o mês e adiciona todos os dados na folha correspondente ao mês;  
- [x] Se não existir uma folha com o mês corrente, esta é criada automaticamente;  
- [x] Backup da planilha antes de qualquer alteração;  
- [x] Não lota o HD de backups, pois mantém o número de backups desejado, excluindo os mais antigos;  
- [x] Vencimento automático com padrão de 1 mês a partir da data de pagamento;
- [x] Opção de inserção de data de pagamento Manual ou Automática (dia de hoje);
- [x] Possibilidade de mudar o padrão de meses para o vencimento;
- [x] Envia mensagens para todos os assinantes na planilha, informando seu vencimento;
- [x] _Caso queira personalizar a mensagem, edite o código na linha 41 e 42 em main.py_  

### Como executar?
 - Windows:  
   Você pode clicar duas vezes em cima de _main.py_ ou abrir o cmd na pasta do programa e escrever:  
   > python main.py  
 - Linux:  
   Inicie um terminal na pasta do arquivo e escreva:  
   > python3 main.py
