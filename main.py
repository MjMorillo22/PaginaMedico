from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
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

# Prueba de búsqueda de un producto
def test_search_product():
    driver.get("https://amadita.com/")
    search_input = driver.find_element_by_name("s")
    search_input.send_keys("prueba")
    search_input.send_keys(Keys.RETURN)
    time.sleep(3)  # Esperar a que carguen los resultados
    assert "prueba" in driver.page_source

# Prueba de navegación por las diferentes secciones
def test_navigation_sections():
    driver.get("https://amadita.com/")
    sections = driver.find_elements_by_css_selector(".nav-link")
    for section in sections:
        section.click()
        time.sleep(2)  # Esperar a que cargue la página
        assert section.text in driver.title

# Prueba de registro de usuario (requiere implementación específica)
def test_user_registration():
    pass

# Prueba de inicio de sesión de usuario (requiere implementación específica)
def test_user_login():
    pass

# Prueba de agregado de un producto al carrito
def test_add_to_cart():
    driver.get("https://amadita.com/")
    product = driver.find_element_by_css_selector(".product")
    add_to_cart_button = product.find_element_by_css_selector(".add_to_cart_button")
    add_to_cart_button.click()
    time.sleep(2)  # Esperar a que se agregue al carrito
    driver.get("https://amadita.com/cart/")
    assert "Tu carrito" in driver.title

# Ejecutar las pruebas
test_search_product()
test_navigation_sections()
# test_user_registration()
# test_user_login()
test_add_to_cart()

# Cerrar el navegador
driver.quit()
