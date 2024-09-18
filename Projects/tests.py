from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Configura el WebDriver (en este caso, Chrome)
driver = webdriver.Chrome()

# Abre la página donde está el formulario
driver.get("http://127.0.0.1:8000/api/categoriaServicios/")

# ===== Prueba 1: Enviar el formulario con datos válidos ===== #
def test_envio_correcto():
    # Encuentra el campo de texto (nombre) y completa con un valor
    nombre_field = driver.find_element(By.NAME, "nombre")
    nombre_field.send_keys("Producto de prueba Amor&Glamour")

    descripcion_field = driver.find_element(By.NAME, "descripcion")
    descripcion_field.send_keys("Producto de prueba")

    # Encuentra el botón por la clase y haz clic para enviar el formulario
    submit_button = driver.find_element(By.CSS_SELECTOR, "button.btn.btn-primary.js-tooltip")
    submit_button.click()

    # Esperar unos segundos para permitir que la respuesta sea procesada
    time.sleep(3)

    # Puedes agregar verificaciones adicionales aquí para asegurarte de que el envío fue exitoso
    print("Formulario enviado correctamente con datos válidos.")

# ===== Prueba 2: Dejar el campo vacío y verificar el mensaje de error ===== #
def test_envio_con_campo_vacio():
    # Refresca la página para empezar la nueva prueba
    driver.refresh()

    # Encuentra el campo de texto (nombre) y asegúrate de que está vacío
    nombre_field = driver.find_element(By.NAME, "nombre")
    nombre_field.clear()

    descripcion_field = driver.find_element(By.NAME, "descripcion")
    descripcion_field.send_keys("Producto de prueba")

    # Encuentra el botón por la clase y haz clic para enviar el formulario
    submit_button = driver.find_element(By.CSS_SELECTOR, "button.btn.btn-primary.js-tooltip")
    submit_button.click()

    # Esperar unos segundos para que aparezca el mensaje de error
    time.sleep(3)

    # Verificar si el mensaje de error aparece
    error_message = driver.find_element(By.CLASS_NAME, "help-block").text

    # Asegúrate de que el mensaje de error sea el correcto
    assert "This field may not be blank" in error_message, "El mensaje de error no coincide o no aparece"
    print("Mensaje de error verificado correctamente.")

# Llamar a las pruebas
try:
    test_envio_correcto()
    test_envio_con_campo_vacio()
finally:
    # Cerrar el navegador al final de todas las pruebas
    driver.quit()