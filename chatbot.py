from selenium import webdriver
import time
#Automação de encaminhamento de mensagens no whatsapp
#Usando a Funcionalidade nativa do whatsapp de encaminhar menssagem
#encaminhar de 5 em 5 menssagens

#Abrir o navegador
navegador = webdriver.Chrome() 
#colocar o navegador em tella cheia
navegador.maximize_window()
#abrir o whatsapp web
navegador.get('https://www.hashtagtreinamentos.com/')
#Tempo para o usuario escanear o QR code
time.sleep(20)
# selecionar um elemento na tela
navegador.find_element('class name', 'botao-verde').click()

#tempo para fechar o navegador apos o uso
time.sleep(50)
