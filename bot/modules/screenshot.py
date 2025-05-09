import base64
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def take_screenshot(driver: WebDriver):
    # Aguarde até que o título "resultados" esteja visível
    wait = WebDriverWait(driver, 10)
    resultados_title = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "h2.chart-title")))

    # Role até Resultados
    driver.execute_script("arguments[0].scrollIntoView({block: 'start'});", resultados_title)

    # Capture a captura de tela
    png = driver.get_screenshot_as_png()
    return base64.b64encode(png).decode('utf-8')
