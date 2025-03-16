from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

# Configurar Selenium en modo headless (sin abrir navegador)
options = webdriver.ChromeOptions()
options.add_argument("--headless")  
options.add_argument("--disable-gpu")  
options.add_argument("--no-sandbox")  
options.add_argument("--disable-dev-shm-usage")

# Iniciar el navegador
driver = webdriver.Chrome(options=options)

# Ir a Instagram
driver.get("https://www.instagram.com/accounts/login/")
time.sleep(3)

# Encontrar campos de usuario y contraseña
username_input = driver.find_element("name", "username")
password_input = driver.find_element("name", "password")

# Ingresar credenciales (reemplazar con tus datos)
username_input.send_keys("tu_usuario")
password_input.send_keys("tu_contraseña")
password_input.send_keys(Keys.RETURN)

time.sleep(5)  # Esperar carga

print("Inicio de sesión exitoso")

# Cerrar navegador
driver.quit()
