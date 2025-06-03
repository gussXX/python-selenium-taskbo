class Automation:
    
    def __init__(self, url: str, driver = None):
    
        self.driver = driver.get(url) if driver else None
        self.url = url
        print("==============================")
        print("Inicializando a automação...")
        print("==============================\n")

    async def get_title(self, driver):
        print("Obtendo o título da página...\n")
        return driver.title
    
    async def get_url(self, driver):
        print("Obtendo a URL da página...\n")
        return driver.current_url
    
    async def get_element_by_css(self, driver, selector):
        print(f"Obtendo o elemento pelo seletor CSS: {selector}\n")
        try:
            element = driver.find_element("css selector", selector)
            return element.text
        except Exception as e:
            print(f"Erro ao obter o elemento: {e}\n")
            return e

    async def get_element_by_xpath(self, driver, xpath):
        print(f"Obtendo o elemento pelo XPath: {xpath}\n")
        try:
            element = driver.find_element("xpath", xpath)
            return element.text
        except Exception as e:
            print(f"Erro ao obter o elemento: {e}\n")
            return e

