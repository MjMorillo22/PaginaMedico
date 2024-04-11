from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Ruta al ejecutable del controlador de Chrome
path_to_chromedriver = 'C:\Files\chromedriver.exe'

# Crear una instancia del servicio ChromeDriver
service = Service(path_to_chromedriver)
service.start()

# Configurar las opciones del navegador (opcional)
options = webdriver.ChromeOptions()
options.add_argument('--ignore-certificate-errors')
options.add_argument('--ignore-ssl-errors')

# Crear una instancia del navegador Chrome
driver = webdriver.Chrome(service=service, options=options)

# URL de la página web a probar (en este caso Wikipedia)
url = "https://es.wikipedia.org"
driver.get(url)

# Prueba 1: Verificar que el título de la página es correcto
expected_title = "Wikipedia, la enciclopedia libre"
assert driver.title == expected_title, f"El título de la página no es {expected_title}"

# Prueba 2: Verificar que el campo de búsqueda está presente y es funcional
wait = WebDriverWait(driver, 10)
search_input = wait.until(EC.element_to_be_clickable((By.NAME, 'search')))
search_input.send_keys("Inteligencia artificial")
search_input.send_keys(Keys.RETURN)
time.sleep(2)  # Esperar a que se cargue la página de resultados
assert "Inteligencia artificial" in driver.title, "No se encontraron resultados de búsqueda"

# Prueba 3: Verificar que el enlace a la página principal está presente y es funcional
driver.switch_to.default_content()  # Switch back to default content in case there's a frame
main_page_link = wait.until(EC.element_to_be_clickable((By.XPATH, '//a[@title="Wikipedia:Portada"]')))
main_page_link.click()
time.sleep(2)  # Esperar a que se cargue la página principal
assert driver.title == expected_title, "No se pudo volver a la página principal de Wikipedia"


# Prueba 4: Verificar que el enlace al portal de la comunidad está presente y es funcional
driver.switch_to.default_content()  # Switch back to default content in case there's a frame
community_portal_link = wait.until(EC.element_to_be_clickable((By.ID, 'n-portal')))
community_portal_link.click()
time.sleep(2)  # Esperar a que se cargue el portal de la comunidad
assert "Portal de la comunidad" in driver.title, "No se pudo acceder al portal de la comunidad"

# Cerrar el navegador
driver.quit()
