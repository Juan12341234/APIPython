import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_envio_correcto():
    driver = webdriver.Chrome()

    driver.get("http://127.0.0.1:8000/api/categoriaServicios/")

    nombre_field = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.NAME, "nombre"))
    )
    nombre_field.clear()
    time.sleep(1)
    nombre_field.send_keys("Producto de prueba Amor&Glamour")

    descripcion_field = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.NAME, "descripcion"))
    )
    descripcion_field.clear()
    time.sleep(1)
    descripcion_field.send_keys("Producto de prueba")

    estado_checkbox = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.NAME, "estado"))
    )
    if not estado_checkbox.is_selected():
        time.sleep(1)
        estado_checkbox.click()

    submit_button = driver.find_element(By.XPATH, "//button[text()='POST']")

    submit_button.click()

    time.sleep(3)

    print("Formulario enviado correctamente con datos válidos.")

    driver.quit()

def test_envio_con_campo_vacio():
    driver = webdriver.Chrome()

    driver.get("http://127.0.0.1:8000/api/categoriaServicios/")

    nombre_field = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.NAME, "nombre"))
    )
    nombre_field.clear()
    time.sleep(1)

    descripcion_field = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.NAME, "descripcion"))
    )
    descripcion_field.clear()
    time.sleep(1)
    descripcion_field.send_keys("Producto de prueba")

    estado_checkbox = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.NAME, "estado"))
    )
    if not estado_checkbox.is_selected():
        time.sleep(1)
        estado_checkbox.click()

    submit_button = driver.find_element(By.XPATH, "//button[text()='POST']")
    submit_button.click()

    error_message = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.CLASS_NAME, "help-block"))
    ).text

    assert "This field may not be blank." in error_message, "El mensaje de error no coincide o no aparece"
    print("Mensaje de error verificado correctamente.")

    driver.quit()

test_envio_correcto()
test_envio_con_campo_vacio()