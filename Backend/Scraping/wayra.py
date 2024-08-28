from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.firefox.options import Options as FirefoxOptions
import pandas as pd
import time
from selenium.common.exceptions import NoSuchElementException, TimeoutException, ElementClickInterceptedException

# Configuration du chemin vers GeckoDriver
driver_path = r"C:\\Program Files (x86)\\geckodriver.exe"  # Remplacez par le chemin vers GeckoDriver

# Configuration des options du navigateur
options = FirefoxOptions()
# options.add_argument('--proxy-server=185.183.33.219')  # Configurez le proxy si nécessaire

# Initialisation du service et du navigateur
service = FirefoxService(executable_path=driver_path)
driver = webdriver.Firefox(service=service, options=options)

# URL de la page à scraper
url = 'https://startups.telefonica.com/'

# Accéder à la page
driver.get(url)

# Attendre que la page soit chargée
WebDriverWait(driver, 30).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "div.row.cardGrid.projects-grid.grid-projects")))

# Fonction pour extraire les informations d'une entreprise
def extract_company_info(element):
    try:
        name = element.find_element(By.CLASS_NAME, 'card-title').text
    except NoSuchElementException:
        name = None

    try:
        industries = element.find_element(By.CSS_SELECTOR, 'div.card-body > p').text
    except NoSuchElementException:
        industries = None

    try:
        description = element.find_element(By.CLASS_NAME, 'card-text text-muted small card-text-description').text
    except NoSuchElementException:
        description = None

    try:
        logo_element = element.find_element(By.TAG_NAME, 'img')
        logo = logo_element.get_attribute('src')
    except NoSuchElementException:
        logo = None

    return {
        "name": name,
        "industries": industries,
        "description": description,
        "logo": logo
    }

# Initialiser la liste pour stocker les données des entreprises
companies = []

# Limiter à 38 pages
max_pages = 38
current_page = 0

while current_page < max_pages:
    print(f"Scraping page {current_page + 1}...")
    
    # Attendre que les éléments de la page soient présents
    WebDriverWait(driver, 30).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, 'div.card')))
    time.sleep(5)
    
    # Trouver tous les éléments d'entreprise sur la page
    company_elements = driver.find_elements(By.CSS_SELECTOR, 'div.card')
    
    # Extraire les informations de chaque entreprise
    for element in company_elements:
        company_info = extract_company_info(element)
        companies.append(company_info)
    
    # Cliquer sur le bouton de la page suivante
    try:
        next_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="pagination"]/div/div'))
        )
        if "disabled" in next_button.get_attribute("class"):
            print("No more pages.")
            break
        driver.execute_script("arguments[0].click();", next_button)  # Utiliser JavaScript pour cliquer
        time.sleep(3)
        current_page += 1
    except (NoSuchElementException, TimeoutException, ElementClickInterceptedException):
        print("No more pages or unable to click.")
        break

# Fermer le navigateur
driver.quit()

# Créer un DataFrame pandas et sauvegarder les données dans un fichier CSV
df = pd.DataFrame(companies)
df.to_csv('company_data_telefonica.csv', index=False)

print("Scraping completed")
