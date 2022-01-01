# Local imports
from recipe_api import app, recipes
import recipe_api.utils as utils

@app.route('/get-recipe-names', methods=['GET'])
def get_recipe_names():
    recipe_names = utils.get_recipe_names(recipes)
    return (
        {'recipes': recipe_names},
        200
    )

@app.route('/recipes/<int:recipe_id>')
def get_recipe_by_id(recipe_id):
    recipe = utils.get_recipe_by_id(recipes, recipe_id)
    return (
        (recipe, 200)
        if recipe is not None else
        ('The recipe with this id does not exist', 404)
    )
