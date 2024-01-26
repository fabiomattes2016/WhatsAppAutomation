import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from webdriver_manager.chrome import ChromeDriverManager
import pyperclip


service = Service(ChromeDriverManager().install())

nav = webdriver.Chrome(service=service)
nav.maximize_window()
nav.get("https://web.whatsapp.com/")

mensagem = """
Este texto foi enviado por mim automaticamente via Python, onde estou testando o selenium para automação de whatsapp! :)
"""

lista_contatos = ["Meu Numero", "Andre Lotus", "Amanda", "ChickCao", "Saulo", "Claudemir de Souza"]

time.sleep(30)

lupa = nav.find_element('xpath', '//*[@id="side"]/div[1]/div/div[2]/button/div[2]/span')
lupa.click()
time.sleep(1)

searchInput = nav.find_element('xpath', '//*[@id="side"]/div[1]/div/div[2]/div[2]/div/div[1]/p')
searchInput.send_keys(lista_contatos[0])
searchInput.send_keys(Keys.ENTER)
time.sleep(2)

messageField = nav.find_element('xpath', '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[1]/p')
pyperclip.copy(mensagem)
messageField.send_keys(Keys.CONTROL + "v")
messageField.send_keys(Keys.ENTER)
time.sleep(2)

qtde_contatos = len(lista_contatos)
qtde_blocos = 0.0

if qtde_contatos % 5 == 0:
    qtde_blocos = qtde_contatos / 5
else:
    qtde_blocos = int(qtde_contatos / 5) + 1

for i in range(qtde_blocos):
    i_inicial = i * 5
    i_final = (i + 1) * 5

    lista_enviar = lista_contatos[i_inicial:i_final]
    lista_elementos = nav.find_elements('class name', '_2AOIt')

    for item in lista_elementos:
        mensagem = mensagem.replace("\n", "")
        texto = item.text.replace("\n", "")

        if mensagem in texto:
            elemento = item

    ActionChains(nav).move_to_element(elemento).perform()
    elemento.find_element('class name', '_3u9t-').click()
    time.sleep(0.5)

    encaminharButton = nav.find_element('xpath', '//*[@id="app"]/div/span[5]/div/ul/div/li[4]/div')
    encaminharButton.click()
    encaminharButtonSelected = nav.find_element('xpath', '//*[@id="main"]/span[2]/div/button[4]/span')
    encaminharButtonSelected.click()
    time.sleep(1)

    for nome in lista_enviar:
        selecionaContatoEncaminhar = nav.find_element(
            'xpath',
            '//*[@id="app"]/div/span[2]/div/div/div/div/div/div/div/div[1]/div/div[2]/div[2]/div/div[1]/p'
        )
        selecionaContatoEncaminhar.send_keys(nome)
        time.sleep(1)
        selecionaContatoEncaminhar.send_keys(Keys.ENTER)
        time.sleep(1)
        selecionaContatoEncaminhar.send_keys(Keys.BACKSPACE)
        time.sleep(1)

    buttonEnviarEncaminhar = nav.find_element(
                'xpath',
                '//*[@id="app"]/div/span[2]/div/div/div/div/div/div/div/span/div/div/div/span'
    )
    buttonEnviarEncaminhar.click()

time.sleep(120)
nav.quit()
