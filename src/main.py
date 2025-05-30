from selenium import webdriver # type: ignore
from selenium.webdriver.chrome.options import Options # type: ignore
from selenium.webdriver.chrome.service import Service # type: ignore
from webdriver_manager.chrome import ChromeDriverManager # type: ignore

options = Options()
options.add_argument('--headless')
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')

# - O WebDriver Manager baixa e instala a versão correta do ChromeDriver, evitando problemas de compatibilidade com o Google Chrome instalado.
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

driver.get("http://selenium.dev")
print(driver.title)
print(driver.current_url)
# print(driver.page_source)
print(driver.find_element("tag name", "h1").text)

driver.close()


