import argparse
from bot.driver import create_driver, accept_cookies
from bot.navigator import navigate_to_page
from bot.extractor import extract_data
from bot.screenshot import take_screenshot
from bot.serializer import serialize_to_json

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--search', required=True, help='CPF ou Nome do beneficiário')
    parser.add_argument('--filters', nargs='*', help='Lista de filtros (ex: servidor programa_social)')
    args = parser.parse_args()

    driver = create_driver()
    driver.get("https://portaldatransparencia.gov.br/pessoa-fisica/busca/lista?pagina=1&tamanhoPagina=10")
    accept_cookies(driver)

    try:
        navigate_to_page(driver, args.search, args.filters)
        data = extract_data(driver)
        screenshot = take_screenshot(driver)
        serialize_to_json(data, screenshot, args.search, args.filters)
    finally:
        driver.quit()

if __name__ == "__main__":
    main()
