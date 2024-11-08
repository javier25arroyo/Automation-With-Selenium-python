from xml.etree.ElementTree import SubElement
from selenium.common.exceptions import TimeoutException, NoSuchElementException 
from selenium.webdriver.support.ui import Select 
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time 
import locale
from datetime import datetime
from dotenv import load_dotenv
import os

load_dotenv()

# Configura la localización a español
locale.setlocale(locale.LC_TIME, 'es_ES.UTF-8')

# Obtiene el número del mes actual
MES = datetime.now().strftime("%m")
print(MES)

# Configurar el navegador
driver = webdriver.Chrome()

USER = "Javier Pérez Arroyo"
ASISTENTE = "Luz Elena Arroyo Rojas"
FECHA_SERVICIO = datetime.now().strftime("%d/%m/%Y")
HORA_ENTRADA = "06"
SALIDA = "00"
HORA_SALIDA = "14"


# Abrir el formulario
driver.get("https://forms.office.com/Pages/ResponsePage.aspx?id=5egoUEctuEmBQDIOQ_X4i-33igUyZuBMpUfJ_czduKtUMUVQT1JESUcwRkJZVE0yS1pYUkxBWU5LWi4u")

title = driver.title

driver.implicitly_wait(0.5)
    
# Llenar el formulario
nombre_usuario = driver.find_element(By.XPATH, '/html/body/div/div/div[1]/div/div/div/div/div[3]/div/div/div[2]/div[2]/div[2]/div[2]/div/span/input')
nombre_usuario.send_keys(USER)
 
nombre_asistente = driver.find_element(By.XPATH, '/html/body/div/div/div[1]/div/div/div/div/div[3]/div/div/div[2]/div[2]/div[3]/div[2]/div/span/input')
nombre_asistente.send_keys(ASISTENTE)
    

fecha_servicio = driver.find_element(By.XPATH, '/html/body/div/div/div[1]/div/div/div/div/div[3]/div/div/div[2]/div[2]/div[4]/div[2]/div/div/div/div/div/input')
fecha_servicio.send_keys(FECHA_SERVICIO)

# Haz clic en el elemento para habilitar el input del mes
driver.find_element(By.XPATH, '//*[@id="question-list"]/div[5]/div[2]/div/div/div').click()
WebDriverWait(driver, 1).until(
    EC.visibility_of_element_located((By.XPATH, '/html/body/div[2]/div'))
)
driver.find_element(By.XPATH, f"/html/body/div[2]/div/div[{int(MES)}]").click()

# Haz clic en el elemento para habilitar el input de la hora de entrada
driver.find_element(By.XPATH, '//*[@id="question-list"]/div[6]/div[2]/div/div/div').click()
WebDriverWait(driver, 1).until(
    EC.visibility_of_element_located((By.XPATH, '/html/body/div[2]/div'))
)
driver.find_element(By.XPATH, f"/html/body/div[2]/div/div[{int(HORA_ENTRADA)}]").click()


# Haz clic en el elemento para habilitar el input de la hora de salida
driver.find_element(By.XPATH, '//*[@id="question-list"]/div[7]/div[2]/div/div/div').click()
WebDriverWait(driver, 1).until(
    EC.visibility_of_element_located((By.XPATH, '/html/body/div[2]/div'))
)
driver.find_element(By.XPATH, f"/html/body/div[2]/div/div[{int(SALIDA) + 1}]").click()


# Haz clic en el elemento para habilitar el input de la hora de salida
driver.find_element(By.XPATH, '//*[@id="question-list"]/div[8]/div[2]/div/div/div').click()

WebDriverWait(driver, 1).until(
    EC.visibility_of_element_located((By.XPATH, '/html/body/div[2]/div'))
)
driver.find_element(By.XPATH, f"/html/body/div[2]/div/div[{int(HORA_SALIDA)}]").click()


# Haz clic en el elemento para habilitar el input de la hora de salida
driver.find_element(By.XPATH, '//*[@id="question-list"]/div[9]/div[2]/div/div/div').click()
WebDriverWait(driver, 1).until(
    EC.visibility_of_element_located((By.XPATH, '/html/body/div[2]/div'))
)
driver.find_element(By.XPATH, f"/html/body/div[2]/div/div[{int(SALIDA) + 1}]").click()

# Haz clic en el botón de enviar
driver.find_element(By.XPATH, '//*[@id="form-main-content1"]/div/div/div[2]/div[3]/div/button').click()


time.sleep(3)
