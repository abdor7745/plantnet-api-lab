"""
'config.py
Defines common constants, such as: paths, colors, icons, ..
author: H.mitiche
update: February 6th 2026
"""

# ---------------- LOCAL PATHS ------------------------

OUTPUT_DIR = "output/"
INPUT_DIR = "input/"
# GPS extraction files
INSECTA_OUTPUT_CSV = OUTPUT_DIR + "insecta_metadata.csv"
FLORA_OUTPUT_CSV = OUTPUT_DIR + "flora_metadata.csv"

# observation images
IMAGES_DIR = INPUT_DIR + "images/"
INSECTA_IMAGES_FOLDER = IMAGES_DIR + "insects/"
FLORA_IMAGES_FOLDER = IMAGES_DIR + "flora/"
FUNGUS_IMAGES_FOLDER = IMAGES_DIR + "fungus/"

# output biodiversity html map
BIODIV_HTML_MAP_FILE = "my_biodiversity_map.html"

# logging filename
LOGFILE = "session.log"

# ----------------- URLS -----------------------------

HF_URL = "https://huggingface.co"

# ----------------- COLORS and ICONS -----------------
# Définition des codes couleurs simples
# ANSI Color Codes
RED = "\033[91m"
YELLOW = "\033[93m"
ORANGE = "\033[38;5;208m"
GREEN = "\033[92m"
BLUE = "\033[94m"
CYAN = "\033[96m"
MAGENTA = "\033[95m"
LIGHT_GREY = "\033[90m"
WHITE = "\033[97m"
# for BOLD characters
BOLD = "\033[1m"
# color reset to default
RESET = "\033[0m"

# Icons with ANSI formatting
ERROR_ICON   = f"{RED}❌{RESET}"
WARNING_ICON = f"{YELLOW}⚠️{RESET}"
WAIT_ICON    = f"{CYAN}⏳{RESET}"       # Changed to Hourglass for 'Wait'
SUCCESS_ICON = f"{GREEN}✅{RESET}"     # Moved checkmark to Success
ROCKET_ICON  = f"{BOLD}🚀{RESET}"
INFO_ICON    = f"{BLUE}ℹ️{RESET}"
DEBUG_ICON   = f"{BOLD}🪲{RESET}"
ZOOM_ICON   = f"\033[38;5;208m🔎\033[0m" # Orange Loupe

# Biology/Science Icons
INSECT_ICON = f"\033[93m🪲\033[0m"  # Yellow/Gold Beetle
FUNGUS_ICON = f"\033[95m🍄\033[0m"  # Magenta Mushroom
PLANT_ICON  = f"\033[92m🌿\033[0m"  # Green Herb/Leaf
MICROSCOPE_ICON = f"{CYAN}🔬{RESET}"       # For analysis/details
TUBE_ICON       = f"{MAGENTA}🧪{RESET}"    # For testing/experiments

# additional utile Icons
QUESTION_ICON   = f"{YELLOW}❓{RESET}"     # For help/missing data
BOOK_ICON       = f"{WHITE}📖{RESET}"      # For documentation/logs
SUMMARY_ICON = f"\033[96m📋\033[0m"  # Cyan Clipboard
TOTALS_ICON  = f"\033[94m📊\033[0m"  # Blue Bar Chart
WWW_ICON = f"\033[94m🌐\033[0m"  # Blue Globe with Meridians
LINK_ICON = f"\033[96m🔗\033[0m" # Cyan Link

# Example Print
#print(f"{MICROSCOPE_ICON} Analyzing data in {OUTPUT_DIR}...")
#print(f"{TUBE_ICON} Running experimental tests...")
