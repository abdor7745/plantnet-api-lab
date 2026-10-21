# 'test_identify_plant.py'
# a test PLANTNET API to identify plants (Botatique only)!
# author: Dr. Hakim Mitiche
# January 2026
# Update: February 14th 2026
import os
import requests
from dotenv import load_dotenv
from pathlib import Path
from PIL import Image
import platform
import subprocess
from config import *

# a function that opens a given folder on explorer
def open_folder(path):
    if platform.system() == "Windows":
        os.startfile(path)
    elif platform.system() == "Darwin":  # macOS
        subprocess.Popen(["open", path])
    else:  # Linux
        subprocess.Popen(["xdg-open", path])

# 1. Configuration des chemins
basedir = "."
dossier_images = basedir + "/images/" 
#fichier_csv = "data_plantnet.csv"
extensions = ('.jpg', '.jpeg', '.png')
# load environment variables in '.env'
load_dotenv()
API_KEY = os.getenv('PLANTNET_API_KEY')
# plant idententification API URL
url = "https://my-api.plantnet.org/v2/identify/all"

# 2. Lister les images dans le repertoire Flora
images_trouvees = [f.name for f in Path(dossier_images).iterdir() if f.suffix.lower() in extensions]

img_count = len(images_trouvees)
print(f"--- Images trouvées ({img_count}) ---")

# Utilisation de enumerate(liste, start=1) pour commencer à compter à 1
for i, img in enumerate(images_trouvees):
    print(f"  [>] {i}: {img}")

# prompt the user to open and check the images folder
answer= input("Do you want to open the images folder? [Y/n]")
if answer == "Y":
    open_folder(dossier_images)

# 3. Inviter l'utilisateur à sélectionner l'image
choix = int(input("\nEntrez le numéro de l'image à identifier : "))
sample_filename = images_trouvees[choix]

identifier_name = "PL@NTPLANET.org"
print(f"\n{MICROSCOPE_ICON}Identification de '{sample_filename}' sur '{identifier_name}' en cours...{WAIT_ICON}")

# 1. Setup the query parameters (API key)
payload = {
    "api-key": API_KEY,
    "include-related-images": "false", # Optional: simplify the response
    "lang": "en" # Optional: language for common names
}

# 2. Setup the image
image_path = dossier_images + sample_filename 
image_data = open(image_path, 'rb')

files = {
    'images': image_data
}

# 3. CRITICAL STEP: Define the organ
# Valid values: 'leaf', 'flower', 'fruit', 'bark', 'auto'
data = {
    'organs': ['auto'] 
}

# 4. Make the POST request
try:
    response = requests.post(url, params=payload, files=files, data=data)
    
    # Check for HTTP errors
    response.raise_for_status() 
    
    # If successful, get and print the top result
    results = response.json()
    best_match = results['results'][0]

    # 1. Accès sécurisé à la Famille (souvent dans 'species')
    #family = best_match.get('species', {}).get('family', {}).get('scientificNameWithoutAuthor', 'Inconnue')

    # 2. Accès aux images de référence (related) fournies par Pl@ntNet :
    images = best_match.get('images', [])
    ref_url = images[0].get('url', {}).get('o', 'Pas d\'image') if images else "Aucune image disponible"

    # 3. Organe le plus probable (Feuille, Fleur, Écorce...)
    """organ : Savoir si l'IA a identifié l'arbre via l'écorce (bark) est vital, 
    car c'est là que les traces de scolytes sont les plus visibles."""
    organ = best_match.get('organ', 'Non spécifié')
    """ gbifId : L'identifiant universel de biodiversité. 
    Très utile pour lier vos données à des bases scientifiques externes comme le GBIF."""
    species_data = best_match.get('species', {})
    gbif_id = species_data.get('gbifId', 'N/A')

    # Extraction des données
    family = best_match['species']['family']['scientificNameWithoutAuthor']
    scientific = best_match['species']['scientificNameWithoutAuthor']
    common = best_match['species']['commonNames'][0]
    #ref_url = best_match['images'][0]['url']['o'] # Lien vers photo de référence
    score = best_match['score'] * 100

    # Affichage "User Friendly"
    print(f"\n{BOLD}{CYAN}🌿 RÉSULTAT DE L'IDENTIFICATION{RESET}")
    print(f"{'─' * 50}")
    print(f"{BOLD}Nom Scientifique : {RESET}{GREEN}{scientific}{RESET}")
    print(f"{BOLD}Nom Commun       : {RESET}{BLUE}{common}{RESET}")
    print(f"{BOLD}Famille          : {RESET}{family}")
    print(f"{BOLD}Confiance        : {RESET}{'✅' if score > 70 else '⚠️ '} {score:.2f}%")
    print(f"{'─' * 50}\n")
    print(f"{BOLD}  Photo Réf.       : {RESET}{LIGHT_GREY}{ref_url}{RESET}")
    print(f"{BOLD}  Organe détecté   : {RESET}{LIGHT_GREY}{organ}{RESET}")
    print(f"{BOLD}  ID GBIF          : {RESET}{gbif_id}")
    
    # Petit rappel pour l'utilisateur
    if "Pinus" in scientific or "Picea" in scientific:
        print(f"{YELLOW}⚠️  Alerte Scolyte : Vérifiez la présence de trous de sortie sur ce genre.{RESET}")

    # show the image
    try:
        r = input("Do you want to see your image?(y/n)")
        if r =="y":
            img_path = os.path.join(dossier_images, sample_filename)
            with Image.open(img_path) as img:
                img.show() # Ouvre la visionneuse Windows/Mac/Linux par défaut
    except Exception as e:
        print(f"{RED}{ERROR_ICON}Erreur lors de l'ouverture de l'image : {e}{RESET}")    

except requests.exceptions.HTTPError as err:
    print(f"HTTP Error: {err}")
    print(response.json()) # Print the API error message for debugging    

finally:
    image_data.close()