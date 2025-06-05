from selenium import webdriver # type: ignore
from selenium.webdriver.chrome.options import Options # type: ignore
from selenium.webdriver.chrome.service import Service # type: ignore
from webdriver_manager.chrome import ChromeDriverManager # type: ignore
from selenium.webdriver.common.by import By # type: ignore

import sys
sys.dont_write_bytecode = True

class Driver:
    def __init__(self):

        options = Options()
        options.add_argument('--headless')
        options.add_argument('--no-sandbox')
        options.add_argument('--disable-dev-shm-usage')
        options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/114.0.5735.90 Safari/537.36")
            
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

    async def set_page(self, url: str):
        if self.driver is None:
            raise Exception("Driver não inicializado. Por favor, inicialize o driver primeiro.")
        
        self.driver.get(url)

        return self.driver


    async def close_driver(self):
        if self.driver is not None:
            self.driver.quit()
            # print("==============================")
            # print("Driver fechado com sucesso!")
            # print("==============================\n")
        else:
            print("Nenhum driver para fechar.")
