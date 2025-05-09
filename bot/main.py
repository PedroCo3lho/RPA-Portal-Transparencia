import argparse
import re
from modules.driver import create_driver, accept_cookies
from modules.navigator import navigate_to_page
from modules.extractor import navigate_and_collect_data
from modules.screenshot import take_screenshot
from modules.serializer import serialize_to_json

def is_valid_input(search):
    # CPF format: XXX.XXX.XXX-XX or XXXXXXXXXXX
    cpf_pattern = r"^\d{3}\.\d{3}\.\d{3}-\d{2}$|^\d{11}$"
    # Name format: Only letters and spaces, at least 5 characters
    name_pattern = r"^[a-zA-ZÀ-ÿ\s]{5,}$"
    return re.match(cpf_pattern, search) or re.match(name_pattern, search)

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--search', required=True, help='CPF ou Nome do beneficiário')
    parser.add_argument('--filters', nargs='*', help='Lista de filtros (ex: servidor programa_social)') # not implemented yet
    args = parser.parse_args()

    # Validate CPF or Name input
    if not is_valid_input(args.search):
        serialize_to_json(None, None, args.search, args.filters, error="Não foi possível retornar os dados no tempo de resposta solicitado")
        print("Erro: CPF ou Nome inválido. Por favor, insira um CPF no formato XXX.XXX.XXX-XX ou um nome válido.")
        return

    driver = create_driver()
    driver.get("https://portaldatransparencia.gov.br/pessoa-fisica/busca/lista?pagina=1&tamanhoPagina=10")
    accept_cookies(driver)

    try:
        # Navigate to the search page and apply filters
        navigate_to_page(driver, args.search)

        # Collect data from the results
        data = navigate_and_collect_data(driver, args.search)
        
        if len(data) == 1 and "error" in data[0]:
            serialize_to_json(None, None, args.search, args.filters, error=data[0]["error"]) 
            print(data[0]["error"])
            return

        # Take a screenshot of the final state
        screenshot = take_screenshot(driver)

        # Serialize the data to JSON
        serialize_to_json(data, screenshot, args.search, args.filters)
    finally:
        driver.quit()

if __name__ == "__main__":
    main()
