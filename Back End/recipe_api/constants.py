# Standard imports
import os

# Third-party imports
from dotenv import load_dotenv

load_dotenv()

RECIPE_FILE = os.getenv('RECIPE_FILE', default='data/temp.json')