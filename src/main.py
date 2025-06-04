from selenium import webdriver # type: ignore
from selenium.webdriver.chrome.options import Options # type: ignore
from selenium.webdriver.chrome.service import Service # type: ignore
from webdriver_manager.chrome import ChromeDriverManager # type: ignore
from selenium.webdriver.common.by import By # type: ignore

import asyncio

from automation.automation  import Automation
from drivers.driver         import Driver
from prices.prices          import Prices

async def main():
    print("Iniciando a aplicação...\n")

    await run_prices()

async def tests():
    # Url desejada para automação
    url = "https://www.magazineluiza.com.br/celular-samsung-galaxy-s25-5g-128gb-12gb-ram-camera-tripla-de-50-12-10-tela-grande-de-6-2/p/gehgkef1jc/te/gs25/"

    # - Inicializa o driver do Selenium, a Aumtomação depende desse driver
    driver = Driver()
    drivers = await driver.init_driver(url = url)

    # - Inicializa a automação com a URL desejada
    automation = Automation(url = url, driver = drivers)

    try:
        # Retorna o título da página
        responde = await automation.get_title(drivers)
        print(f'{responde}\n')

        #retorna a URL da página
        responde = await automation.get_url(drivers)
        print(f'{responde}\n')

        # Retorna o elemento pelo seletor CSS
        responde = await automation.get_element_by_css(drivers, selector = "h1")
        print(f'{responde}\n')

        # Retorna o elemento pelo XPath
        responde = await automation.get_element_by_xpath(drivers, xpath = "//p[contains(@class, 'sc-dcJsrY') and contains(@class, 'eLxcFM') and contains(@class, 'sc-hgRRfv') and contains(@class, 'dfAhbD')]")
        print(f'{responde}\n')

    except Exception as e:
        print(f"Erro ao inicializar a automação: {e}")

    finally:
        # Fechando o driver
        await driver.close_driver()

async def run_prices():

    prices = Prices(links = [
        "https://www.magazineluiza.com.br/celular-samsung-galaxy-s25-5g-128gb-12gb-ram-camera-tripla-de-50-12-10-tela-grande-de-6-2/p/gehgkef1jc/te/gs25/",
        "https://www.magazineluiza.com.br/apple-iphone-16e-128gb-branco-61-48mp-ios-5g/p/240059700/te/i16e/",
        "https://www.magazineluiza.com.br/apple-iphone-14-128gb-estelar-61-12mp-ios-5g/p/237184100/te/ip14/"
    ])

    prices_response = await prices.get_prices(links = prices.links)
    print(prices_response)



asyncio.run(main())


