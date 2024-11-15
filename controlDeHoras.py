from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from datetime import datetime
from dotenv import load_dotenv
import locale
import os
import time

def setup_locale():
    locale.setlocale(locale.LC_TIME, 'es_ES.UTF-8')

def get_current_month():
    return datetime.now().strftime("%m")

def get_current_date():
    return datetime.now().strftime("%d/%m/%Y")

def load_env_variables():
    load_dotenv()
    return {
        "USER": "Javier Pérez Arroyo",
        "ASISTENTE": "Luz Elena Arroyo Rojas",
        "FECHA_SERVICIO": get_current_date(),
        "HORA_ENTRADA": "06",
        "SALIDA": "00",
        "HORA_SALIDA": "14"
    }

def setup_driver():
    driver = webdriver.Chrome()
    driver.implicitly_wait(0.5)
    return driver

def fill_form(driver, user_data):
    driver.get("https://forms.office.com/Pages/ResponsePage.aspx?id=5egoUEctuEmBQDIOQ_X4i-33igUyZuBMpUfJ_czduKtUMUVQT1JESUcwRkJZVE0yS1pYUkxBWU5LWi4u")

    form_fields = [
        ('/html/body/div/div/div[1]/div/div/div/div/div[3]/div/div/div[2]/div[2]/div[2]/div[2]/div/span/input', user_data["USER"]),
        ('/html/body/div/div/div[1]/div/div/div/div/div[3]/div/div/div[2]/div[2]/div[3]/div[2]/div/span/input', user_data["ASISTENTE"]),
        ('/html/body/div/div/div[1]/div/div/div/div/div[3]/div/div/div[2]/div[2]/div[4]/div[2]/div/div/div/div/div/input', user_data["FECHA_SERVICIO"])
    ]

    for xpath, value in form_fields:
        element = driver.find_element(By.XPATH, xpath)
        element.send_keys(value)

    select_dropdown(driver, '//*[@id="question-list"]/div[5]/div[2]/div/div/div', int(get_current_month()))
    select_dropdown(driver, '//*[@id="question-list"]/div[6]/div[2]/div/div/div', int(user_data["HORA_ENTRADA"]))
    select_dropdown(driver, '//*[@id="question-list"]/div[7]/div[2]/div/div/div', int(user_data["SALIDA"]) + 1)
    select_dropdown(driver, '//*[@id="question-list"]/div[8]/div[2]/div/div/div', int(user_data["HORA_SALIDA"]))
    select_dropdown(driver, '//*[@id="question-list"]/div[9]/div[2]/div/div/div', int(user_data["SALIDA"]) + 1)

    time.sleep(5)
    driver.find_element(By.XPATH, '//*[@id="form-main-content1"]/div/div/div[2]/div[3]/div/button').click()

def select_dropdown(driver, dropdown_xpath, option_index):
    driver.find_element(By.XPATH, dropdown_xpath).click()
    WebDriverWait(driver, 1).until(
        EC.visibility_of_element_located((By.XPATH, '/html/body/div[2]/div'))
    )
    driver.find_element(By.XPATH, f"/html/body/div[2]/div/div[{option_index}]").click()

def main():
    setup_locale()
    user_data = load_env_variables()
    driver = setup_driver()
    try:
        fill_form(driver, user_data)
    finally:
        driver.quit()

if __name__ == "__main__":
    main()
