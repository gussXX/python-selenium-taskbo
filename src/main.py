from selenium import webdriver # type: ignore
from selenium.webdriver.chrome.options import Options # type: ignore
from selenium.webdriver.chrome.service import Service # type: ignore
from webdriver_manager.chrome import ChromeDriverManager # type: ignore
from selenium.webdriver.common.by import By # type: ignore

options = Options()
options.add_argument('--headless')
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')
options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/114.0.5735.90 Safari/537.36")

# - O WebDriver Manager baixa e instala a versão correta do ChromeDriver, evitando problemas de compatibilidade com o Google Chrome instalado.
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

driver.get("https://www.magazineluiza.com.br/celular-samsung-galaxy-s25-5g-128gb-12gb-ram-camera-tripla-de-50-12-10-tela-grande-de-6-2/p/gehgkef1jc/te/gs25/")

print(driver.title)
print(driver.current_url)

print(driver.find_element("xpath", "//p[contains(@class, 'sc-dcJsrY') and contains(@class, 'eLxcFM') and contains(@class, 'sc-hgRRfv') and contains(@class, 'dfAhbD')]").text)

# print(driver.page_source)
# print(driver.find_element("css selector", ".h3.mb-3.selenium-ide").text)

# # Seleciona o elemento com a classe h3, mb-3 e selenium-ide, restringindo a busca ao elemento <h4> que contém essas classes.
# print(driver.find_element("xpath", "//h4[contains(@class, 'h3') and contains(@class, 'mb-3') and contains(@class, 'selenium-ide')]").text)

driver.close()


