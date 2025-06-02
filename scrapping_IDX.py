import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def scrape_companyprofile_idx(emiten, output_file='companyprofile_idx.json'):
    """
    scrapping company profile from IDX using emiten code
    :param emiten (list): emiten code
    :param output_file:
    :return:
    """
    all_data = []

    for id_ in emiten:
        url = f"https://www.idx.co.id/id/perusahaan-tercatat/profil-perusahaan-tercatat/{id_}"

        options = Options()
        options.add_argument('--no-sandbox')
        options.add_argument('--disable-dev-shm-usage')

        driver = webdriver.Chrome(options=options)
        wait = WebDriverWait(driver, 20)

        print(f"Memproses ID: {id_}")
        data = {"ID": id_}

        try:
            driver.get(url)
            wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "section.container.mb-48")))

            rows = driver.find_elements(By.CSS_SELECTOR, "section.container.mb-48 table tr")
            for row in rows:
                try:
                    key_elem = row.find_element(By.CSS_SELECTOR, "td.td-name")
                    val_elem = row.find_element(By.CSS_SELECTOR, "td.td-content")
                    key = key_elem.text.strip()
                    val = val_elem.text.strip()
                    if key and val:
                        data[key] = val
                except:
                    continue

            all_data.append(data)

        except Exception as e:
            print(f"Gagal memproses ID {id_}: {e}")
            driver.save_screenshot(f"error_{id_}.png")

        finally:
            driver.quit()

    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(all_data, f, ensure_ascii=False, indent=4)

    print(f"Data disimpan ke '{output_file}'")
    return all_data


