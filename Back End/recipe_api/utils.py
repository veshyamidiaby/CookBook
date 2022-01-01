# Standard imports
import json
from typing import Dict, List, Optional

# Local imports
from recipe_api.constants import RECIPE_FILE

def get_recipe_by_id(recipe_list: List, recipe_id: int) -> Optional[Dict]:
    """
    Obtain a recipe with the specified id from a given list of recipes
    
    Input:      recipe_list -> List
                recipe_id -> int
    Output:     recipe -> List[str] or None
    """
    for recipe in recipe_list:
        if recipe.get('id') == recipe_id:
            return recipe
    return None

def get_recipe_names(recipe_list: List) -> List[str]:
    """
    Extract the names of the recipes within a given list
    
    Input:      recipe_list -> List
    Output:     recipe_names -> List[str]
    """
    recipe_names: List[str] = []

    for recipe in recipe_list:
        recipe_names.append(recipe.get('name'))

    return recipe_names

def load_recipe_data():
    """
    Extract data from the recipe file and return its contents
    
    Input:      None
    Output:     None
    """
    recipe_file = open(RECIPE_FILE, 'r').read()
    return json.loads(recipe_file)['recipes']
