from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.firefox.options import Options as FirefoxOptions
import pandas as pd
import time
from selenium.common.exceptions import NoSuchElementException, TimeoutException

# Configuration du chemin vers GeckoDriver
driver_path = r"C:\\Program Files (x86)\\geckodriver.exe"  # Remplacez par le chemin vers GeckoDriver

# Configuration des options du navigateur
options = FirefoxOptions()
#options.add_argument('--proxy-server=185.177.125.213')  # Configurez le proxy si nécessaire

# Initialisation du service et du navigateur
service = FirefoxService(executable_path=driver_path)
driver = webdriver.Firefox(service=service, options=options)

# URL de la page à scraper
url = 'https://www.crunchbase.com/discover/organization.companies'

# Accéder à la page
driver.get(url)

# Attendre que la page soit chargée
WebDriverWait(driver, 30).until(EC.visibility_of_element_located((By.CLASS_NAME, "ng-star-inserted")))
time.sleep(1)

# Fonction pour extraire les informations d'une entreprise
def extract_company_info(element):
    cells = element.find_elements(By.TAG_NAME, 'grid-cell')
    
    name = cells[1].text if len(cells) > 1 else None  # Suppose que le nom est dans le deuxième grid-cell
    industries = cells[2].text if len(cells) > 2 else None  # Suppose que les industries sont dans le troisième grid-cell
    location = cells[3].text if len(cells) > 3 else None  # Suppose que la location est dans le quatrième grid-cell
    description = cells[4].text if len(cells) > 4 else None  # Suppose que la description est dans le cinquième grid-cell
    cb = cells[5].text if len(cells) > 5 else None  # Suppose que cb est dans le sixième grid-cell

    return {
        "name": name,
        "industries": industries,
        "location": location,
        "description": description,
        "cb": cb
    }

# Initialiser la liste pour stocker les données des entreprises
companies = []

# Limiter à 20 pages
max_pages = 20
current_page = 0

while current_page < max_pages:
    print(f"Scraping page {current_page + 1}...")
    
    # Attendre que les éléments de la page soient présents
    WebDriverWait(driver, 30).until(EC.presence_of_all_elements_located((By.TAG_NAME, 'grid-row')))  # Changez ce sélecteur selon la structure réelle
    time.sleep(5)
    
    # Trouver tous les éléments d'entreprise sur la page
    company_elements = driver.find_elements(By.TAG_NAME, 'grid-row')  # Changez ce sélecteur selon la structure réelle
    
    # Extraire les informations de chaque entreprise
    for element in company_elements:
        company_info = extract_company_info(element)
        companies.append(company_info)
    
    # Cliquer sur le bouton de la page suivante
    try:
        next_button = driver.find_element(By.CSS_SELECTOR, 'button[aria-label="Next page"]')  # Changez ce sélecteur selon la structure réelle
        if "disabled" in next_button.get_attribute("class"):
            print("No more pages.")
            break
        next_button.click()
        
        # Attendre que la nouvelle page se charge
        WebDriverWait(driver, 30).until(EC.presence_of_all_elements_located((By.TAG_NAME, 'grid-row')))
        time.sleep(5)
        
        current_page += 1
    except NoSuchElementException:
        print("No more pages.")
        break

# Fermer le navigateur
driver.quit()

# Créer un DataFrame pandas et sauvegarder les données dans un fichier CSV
df = pd.DataFrame(companies)
df.to_csv('company_data_new4.csv', index=False)

print("Scraping completed")
