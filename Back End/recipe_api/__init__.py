# Standard imports
from flask import Flask
from typing import List

# Local imports
from recipe_api.utils import load_recipe_data

app: Flask = Flask(__name__)

recipes: List = load_recipe_data()

# Required for routes to be functional
from recipe_api import routes