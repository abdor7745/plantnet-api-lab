# 'test_identify_plant.py'
# a test PLANTNET API to identify plants (Botatique only)!
# author: Dr. Hakim Mitiche
# January 2026
# Update: February 14th 2026
import os
import platform
import subprocess
from pathlib import Path
from config import *
from PIL import Image
from dotenv import load_dotenv
import requests


# a function that opens a given folder on explorer

def open_folder(path):
  # On convertit le chemin relatif en chemin absolu pour éviter les erreurs sous Windows
  abs_path = os.path.abspath(path)
  if platform.system() == "Windows":
    os.startfile(abs_path)
  elif platform.system() == "Darwin":  # macOS
    subprocess.Popen(["open", abs_path])
  else:  # Linux
    subprocess.Popen(["xdg-open", abs_path])


# 1. Configuration des chemins
basedir = "."
dossier_images = basedir + "/images/"
# fichier_csv = "data_plantnet.csv"
extensions = (".jpg", ".jpeg", ".png")
# load environment variables in '.env'
load_dotenv()
API_KEY = os.getenv("PLANTNET_API_KEY")
# plant idententification API URL
url = "https://my-api.plantnet.org/v2/identify/all"

# 2. Lister les images dans le repertoire Flora
images_trouvees = [
    f.name for f in Path(dossier_images).iterdir() if f.suffix.lower() in extensions
]

img_count = len(images_trouvees)
print(f"--- Images trouvées ({img_count}) ---")

# Utilisation de enumerate(liste, start=1) pour commencer à compter à 1
for i, img in enumerate(images_trouvees):
  print(f"  [>] {i}: {img}")

# prompt the user to open and check the images folder
answer = input("Do you want to open the images folder? [Y/n]")
if answer == "Y":
  open_folder(dossier_images)

# 3. Inviter l'utilisateur à sélectionner l'image
choix = int(input("\nEntrez le numéro de l'image à identifier : "))
sample_filename = images_trouvees[choix]

identifier_name = "PL@NTPLANET.org"
print(
    f"\n{MICROSCOPE_ICON}Identification de '{sample_filename}' sur"
    f" '{identifier_name}' en cours...{WAIT_ICON}"
)

# 1. Setup the query parameters (API key)
payload = {
    "api-key": API_KEY,
    "include-related-images": "false",  # Optional: simplify the response
    "lang": "en",  # Optional: language for common names
}

# 2. Setup the image
image_path = dossier_images + sample_filename
image_data = open(image_path, "rb")

files = {"images": image_data}

# 3. CRITICAL STEP: Define the organ
# Valid values: 'leaf', 'flower', 'fruit', 'bark', 'auto'
data = {"organs": ["auto"]}

# 4. Make the POST request

try:
  response = requests.post(url, params=payload, files=files, data=data)

  # Si l'API renvoie 404 (Species not found)
  if response.status_code == 404:
    print(
        f"\n{YELLOW}⚠️ L'API PlantNet n'a pu identifier aucune espèce pour cette"
        f" image (404 : Species not found).{RESET}"
    )
    print(
        "Essayez avec une autre image plus nette ou montrant des feuilles/fleurs"
        " caractéristiques.\n"
    )

  else:
    # Pour tout autre code d'erreur HTTP non géré
    response.raise_for_status()

    # Si c'est un succès (200 OK), on traite les résultats...
    results = response.json().get("results", [])

    if results:
      best_match = results[0]

      # Extraction des données principales
      species_data = best_match.get("species", {})
      family = species_data.get("family", {}).get(
          "scientificNameWithoutAuthor", "Inconnue"
      )
      scientific = species_data.get("scientificNameWithoutAuthor", "Inconnu")
      common_names = species_data.get("commonNames", [])
      common = common_names[0] if common_names else "Aucun nom commun"

      # Images de référence
      images = best_match.get("images", [])
      ref_url = (
          images[0].get("url", {}).get("o", "Pas d'image")
          if images
          else "Aucune image disponible"
      )

      organ = best_match.get("organ", "Non spécifié")
      gbif_id = species_data.get("gbifId", "N/A")
      score = best_match.get("score", 0.0) * 100

      # Affichage "User Friendly" du meilleur résultat
      print(f"\n{BOLD}{CYAN}🌿 RÉSULTAT DE L'IDENTIFICATION{RESET}")
      print(f"{'─' * 50}")
      print(f"{BOLD}Nom Scientifique : {RESET}{GREEN}{scientific}{RESET}")
      print(f"{BOLD}Nom Commun       : {RESET}{BLUE}{common}{RESET}")
      print(f"{BOLD}Famille          : {RESET}{family}")
      print(
          f"{BOLD}Confiance        : {RESET}{'✅' if score > 70 else '⚠️ '} {score:.2f}%"
      )
      print(f"{'─' * 50}\n")
      print(f"{BOLD}  Photo Réf.       : {RESET}{LIGHT_GREY}{ref_url}{RESET}")
      print(f"{BOLD}  Organe détecté   : {RESET}{LIGHT_GREY}{organ}{RESET}")
      print(f"{BOLD}  ID GBIF          : {RESET}{gbif_id}")

      # Affichage du Top 3 des prédictions
      print(f"\n{BOLD}{CYAN}--- TOP 3 DES PRÉDICTIONS ---{RESET}")
      print(f"{'─' * 50}")
      for idx, res in enumerate(results[:3], start=1):
        species_name = (
            res.get("species", {}).get("scientificNameWithoutAuthor", "Inconnu")
        )
        top_score = res.get("score", 0.0) * 100
        print(f"{BOLD}{idx}. {species_name} — Confiance : {top_score:.2f}%{RESET}")
      print(f"{'─' * 50}\n")

      # Petit rappel pour l'utilisateur
      if "Pinus" in scientific or "Picea" in scientific:
        print(
            f"{YELLOW}⚠️  Alerte Scolyte : Vérifiez la présence de trous de sortie"
            f" sur ce genre.{RESET}"
        )

      # show the image
      try:
        r = input("Do you want to see your image?(y/n)")
        if r == "y":
          img_path = os.path.join(dossier_images, sample_filename)
          with Image.open(img_path) as img:
            img.show()
      except Exception as e:
        print(
            f"{RED}{ERROR_ICON}Erreur lors de l'ouverture de l'image :"
            f" {e}{RESET}"
        )

    else:
      print(
          f"{YELLOW}⚠️ La liste des résultats est trouvée mais est vide par"
          f" l'API.{RESET}"
      )
except requests.exceptions.ConnectTimeout:
  print(
      f"\n{RED}⏱️ Erreur de connexion : Le serveur a mis trop de temps à"
      f" répondre (Timeout). Vérifiez votre connexion internet et"
      f" réessayez.{RESET}"
  )
except requests.exceptions.RequestException as err:
  print(f"\n{RED}❌ Erreur réseau : {err}{RESET}")

except requests.exceptions.HTTPError as err:
  print(f"HTTP Error: {err}")
  if "response" in locals() and response is not None:
    print(response.json())

finally:
  image_data.close()