from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
from selenium.webdriver.common.keys import Keys

# Configurar ChromeOptions para depuración remota
options = webdriver.ChromeOptions()
options.add_experimental_option("debuggerAddress", "localhost:9222")  # Conectar al puerto de depuración

# Iniciar el WebDriver conectando a la sesión remota de Chrome
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

# Ahora deberías estar conectado a la instancia de Chrome que abriste manualmente
# Esperar un poco para asegurarse de que la página está cargada
time.sleep(5)

# Localizar el botón usando XPath con el texto "Nuevo MDS"
button = driver.find_element(By.XPATH, "//div[contains(text(),'Nuevo MDS')]")


# Hacer clic en el botón
button.click()

# Esperar un poco para ver el resultado
time.sleep(5)

# Enviar el número 2014
driver.switch_to.active_element.send_keys("2014")

# Enviar la tecla Tab para moverse al siguiente campo
driver.switch_to.active_element.send_keys(Keys.TAB)

# Esperar un poco para asegurarse de que el cursor se ha movido al siguiente campo
time.sleep(1)  # Ajusta si es necesario

# Ahora puedes ingresar más datos en el siguiente campo si es necesario
driver.switch_to.active_element.send_keys("9263464")

# Mantener el navegador abierto hasta que el usuario presione Enter
input("Presiona Enter para cerrar el navegador...")

# Cerrar el navegador
driver.quit()



