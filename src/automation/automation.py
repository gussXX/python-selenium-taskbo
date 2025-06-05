import sys
sys.dont_write_bytecode = True

class Automation:
    
    def __init__(self, url: str, driver = None):
    
        self.driver = driver.get(url) if driver else None
        self.url = url


    async def get_title(self, driver):
        # print("Obtendo o título da página...")

        return driver.title
    
    async def get_url(self, driver):
        # print("Obtendo a URL da página...")
        return driver.current_url
    
    async def get_element_by_css(self, driver, selector):
        # print(f"Obtendo o elemento pelo seletor CSS: {selector}")
        try:
            element = driver.find_element("css selector", selector)
            return element.text
        except Exception as e:
            print(f"Erro ao obter o elemento: {e}")

            return e

    async def get_element_by_xpath_1(self, driver, xpath):
        # print(f"Obtendo o elemento pelo XPath: {xpath}")
        try:
            element = driver.find_element("xpath", xpath)

            if "ou R$ " in element.text:
                string = element.text
                response = string.replace("ou R$ ", "").replace(" ", "").replace("R$", "")
                
                return response
        
            else:

                return element.text
        
        except Exception as e:
            print(f"Erro ao obter o elemento: {e}")
            
            return e
        
    async def get_element_by_xpath(self, driver, xpath):

        try:
            element = driver.find_element("xpath", xpath)
            return element

        except Exception as e:
            print(f"Erro ao obter o elemento: {e}")
            
            return e
        
    async def get_elements_by_xpath(self, driver, xpath):

        try:
            element = driver.find_elements("xpath", xpath)
            return element

        except Exception as e:
            print(f"Erro ao obter o elemento: {e}")
            
            return e

