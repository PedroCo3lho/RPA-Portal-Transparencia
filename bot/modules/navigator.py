import time
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.webdriver import WebDriver


# Mapear os IDs dos filtros disponíveis
FILTER_IDS = {
    "servidor": "servidorPublico",
    "programa_social": "beneficiarioProgramaSocial",
    "cpgf": "portadorCPGF",
    "cpdc": "portadorCPDC",
    "sancao": "sancaoVigente",
    "imovel_funcional": "ocupanteImovelFuncional",
    "contrato": "possuiContrato",
    "favorecido": "favorecidoRecurso",
    "emitente_nfe": "emitenteNfe"
}

def navigate_to_page(driver: WebDriver, search: str):
    search_input = driver.find_element(By.ID, "termo")
    search_input.clear()
    search_input.send_keys(search)
    assert search_input.get_attribute("value") == search

    # Aguarde até que o botão esteja visível e clicável
    form = driver.find_element(By.ID, 'form-consulta')
    form.submit()
    time.sleep(2)  # Aguarde um pouco para garantir que a página carregou completamente
    # Verifica se há resultados
