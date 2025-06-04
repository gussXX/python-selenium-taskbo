# Essa classe é responsavel por receber uma lista de links para buscar os preços dos produtos

from drivers.driver import Driver
from automation.automation import Automation

class Prices:

    def __init__(self, links: list[str]):

        self.links = links

    async def get_prices(self, links: list[str]) -> list[str]:

        driver = Driver()
        responses = []

        for link in links:

            drivers = await driver.init_driver(url = link)
            automation = Automation(url = link, driver = drivers)

            try:
                responde = await automation.get_element_by_xpath(
                    drivers, xpath = ""
                    "//p[contains(@class, 'sc-dcJsrY') "
                    "and contains(@class, 'eLxcFM') "
                    "and contains(@class, 'sc-hgRRfv') "
                    "and contains(@class, 'dfAhbD')]")
                print(f'{responde}\n')

                responses.append(responde)

            except Exception as e:
                print(f"Erro ao inicializar a automação: {e}")
        
        await driver.close_driver()

        return responses





    