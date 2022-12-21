import requests
import json


def api_call(cuisine):
    payload = {'apiKey':'3888fcd00cc145eda0180b67fc4dd822',
    'number': 3,
    'tags':cuisine}

    search = requests.get('https://api.spoonacular.com/recipes/random', params=payload)

    results = search.json() 
    recipes = results.get('recipes')
    

    i = 1
    new_dict = {}
    for recipe in recipes:
        recipe = json.loads(json.dumps(recipe))
        title = recipe.get('title')
        print(title)

        servings = recipe.get('servings')
        readyInMinutes = recipe.get('readyInMinutes')
        instructions = recipe.get('instructions')
        ingredients = recipe.get('extendedIngredients')
        new_dict[f'recipe{i}'] = {
        
        "title" : title,
        "servings" : servings,
        "readyInMinutes" : readyInMinutes,
        "instructions" : instructions,
        "ingredients" : ingredients
        }
        i += 1 
    print(new_dict)
    return new_dict
        

# api_call('mediterranean')
# api_call('mediterranean')

