from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.webdriver import WebDriver

def extract_data(driver: WebDriver):
    resultados = []
    try:
        # Encontra todos os blocos de resultado individual
        itens = driver.find_elements(By.CSS_SELECTOR, "#resultados .br-item")
        
        for item in itens:
            try:
                nome = item.find_element(By.CSS_SELECTOR, ".link-busca-nome").text
                cpf = item.find_element(By.XPATH, ".//strong[contains(text(), 'CPF')]").text
                # A descrição é a última div dentro do item
                descricao = item.find_elements(By.CSS_SELECTOR, ".col-sm-12")[-1].text

                resultados.append({
                    "nome": nome,
                    "cpf": cpf,
                    "descricao": descricao
                })
            except Exception as e:
                resultados.append({"error": f"Erro em item individual: {str(e)}"})
    except Exception as e:
        return {"error": f"Erro ao encontrar lista de resultados: {str(e)}"}

    return resultados
