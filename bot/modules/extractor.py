from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def navigate_and_collect_data(driver):
    base_url = "https://portaldatransparencia.gov.br"
    results = []

    while True:  # Loop to handle pagination
        # Wait for the results to load
        WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".link-busca-nome"))
        )

        # Locate all names in the results
        items = driver.find_elements(By.CSS_SELECTOR, ".link-busca-nome")
        for index, item in enumerate(items):
            try:
                # Re-locate the item to avoid stale element reference
                items = driver.find_elements(By.CSS_SELECTOR, ".link-busca-nome")
                item = items[index]

                # Extract name and CPF from the results page
                name = item.text
                cpf = driver.find_elements(By.CSS_SELECTOR, ".br-item strong")[index].text

                # Get the link and ensure it's a full URL
                link = item.get_attribute("href")
                if not link.startswith("http"):  # Check if the link is relative
                    link = f"{base_url}{link}"  # Concatenate base_url with the relative link

                print(f"Navigating to: {link}")  # Debugging the URL
                driver.get(link)

                # Wait for the detailed page to load
                WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located((By.CSS_SELECTOR, ".dados-tabelados"))
                )

                # Extract detailed data
                detailed_data = extract_detailed_data(driver)

                # Append the data to results
                results.append({
                    "name": name,
                    "cpf": cpf,
                    "details": detailed_data
                })

                # Navigate back to the results page
                driver.back()

                # Wait for the results page to load again
                WebDriverWait(driver, 10).until(
                    EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".link-busca-nome"))
                )

            except Exception as e:
                results.append({
                    "name": name if 'name' in locals() else "Unknown",
                    "error": str(e)
                })

        # Check if there is a "Next" button for pagination
        try:
            next_button = driver.find_element(By.CSS_SELECTOR, ".pagination .next a")
            if "disabled" in next_button.get_attribute("class"):
                break  # Exit the loop if the "Next" button is disabled
            next_button.click()

            # Wait for the next page to load
            WebDriverWait(driver, 10).until(
                EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".link-busca-nome"))
            )
        except Exception:
            break  # Exit the loop if no "Next" button is found

    return results

def extract_detailed_data(driver):
    data = {}

    try:
        # Extract general information
        name = driver.find_element(By.CSS_SELECTOR, ".dados-tabelados .col-sm-4 span").text.strip()
        cpf = driver.find_element(By.CSS_SELECTOR, ".dados-tabelados .col-sm-3 span").text.strip()
        location = driver.find_element(By.CSS_SELECTOR, ".dados-tabelados .col-sm-3:nth-child(3) span").text.strip()

        data["name"] = name
        data["cpf"] = cpf
        data["location"] = location

        # Click on "Recebimentos de recursos"
        try:
            recebimentos_button = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, "button[aria-controls='accordion-recebimentos-recursos']"))
            )
            recebimentos_button.click()
            time.sleep(2)

            # Extract data from all resource tables
            data["resources"] = extract_resource_tables(driver)

        except Exception as e:
            data["resources_error"] = f"Error accessing resources: {str(e)}"

    except Exception as e:
        data["error"] = f"Error extracting detailed data: {str(e)}"

    return data

def extract_resource_tables(driver):
    resources = []

    # Locate all resource tables
    tables = driver.find_elements(By.CSS_SELECTOR, ".br-table")
    for table in tables:
        try:
            rows = table.find_elements(By.CSS_SELECTOR, "tbody tr")

            for row in rows:
                try:
                    detalhar_link = row.find_element(By.CSS_SELECTOR, ".noprint a").get_attribute("href")

                    resources.append({
                        "detalhar_link": detalhar_link,
                    })
                except Exception as e:
                    resources.append({"error": f"Error extracting row data: {str(e)}"})

        except Exception as e:
            resources.append({"error": f"Error extracting table data: {str(e)}"})

    return resources


