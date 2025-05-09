from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def create_driver():
    options = webdriver.EdgeOptions()
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument('--window-size=1920,1080')
    return webdriver.Edge(options=options)

def accept_cookies(driver):
    try:
        # Aguarde até que o botão de cookies esteja visível
        wait = WebDriverWait(driver, 10)
        cookie_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Aceitar')]")))
        cookie_button.click()
    except Exception as e:
        print("Botão de cookies não encontrado ou já aceito:", e)