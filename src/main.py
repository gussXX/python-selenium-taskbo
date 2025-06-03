from selenium import webdriver # type: ignore
from selenium.webdriver.chrome.options import Options # type: ignore
from selenium.webdriver.chrome.service import Service # type: ignore
from webdriver_manager.chrome import ChromeDriverManager # type: ignore
from selenium.webdriver.common.by import By # type: ignore

import sys
import asyncio

from automation.automation import Automation
from drivers.driver import Driver

async def main():

    # options = Options()
    # options.add_argument('--headless')
    # options.add_argument('--no-sandbox')
    # options.add_argument('--disable-dev-shm-usage')
    # options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/114.0.5735.90 Safari/537.36")
    # # - O WebDriver Manager baixa e instala a versão correta do ChromeDriver, evitando problemas de compatibilidade com o Google Chrome instalado.
    # driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

    # Url desejada para automação
    url = "https://www.magazineluiza.com.br/celular-samsung-galaxy-s25-5g-128gb-12gb-ram-camera-tripla-de-50-12-10-tela-grande-de-6-2/p/gehgkef1jc/te/gs25/"

    driver = Driver()

    # Inicializa o driver
    drivers = await driver.init_driver(url = url)

    # - Inicializa a automação com a URL desejada
    automation = Automation(url = url, driver = drivers)

    # driver.get(url)

    # Retorna o título da página
    responde = await automation.get_title(drivers)
    print("==============================")
    print(responde)
    print("==============================\n")

    #retorna a URL da página
    responde = await automation.get_url(drivers)
    print("==============================")
    print(responde)
    print("==============================\n")

    # Retorna o elemento pelo seletor CSS
    responde = await automation.get_element_by_css(drivers, selector = "h1")
    print("==============================")
    print(responde)
    print("==============================\n")

    # Retorna o elemento pelo XPath
    responde = await automation.get_element_by_xpath(drivers, xpath = "//p[contains(@class, 'sc-dcJsrY') and contains(@class, 'eLxcFM') and contains(@class, 'sc-hgRRfv') and contains(@class, 'dfAhbD')]")
    print("==============================")
    print(responde)
    print("==============================\n")


    # driver.close()

asyncio.run(main())


