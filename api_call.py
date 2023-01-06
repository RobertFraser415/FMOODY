import requests
import json



def api_call(cuisine):
    payload = {'apiKey':'3888fcd00cc145eda0180b67fc4dd822',
    # payload = {'apiKey':'ede5e343794c4af684778c4403cd197c',
    'number': 25,
    # triying jinja to fix the random button ?? 
    # {% if cuisine="random": %}
    'tags': cuisine}
    # {% %}

    search = requests.get('https://api.spoonacular.com/recipes/random', params=payload)

    results = search.json() 
    
    recipes = results.get('recipes')
    

    i = 1
    new_dict = {}
    for recipe in recipes:
        recipe = json.loads(json.dumps(recipe))

        title = recipe.get('title')
        # title = '"' + title[0:] + '"'
        servings = recipe.get('servings')
        # servings = '"' + servings[1:-2] + '"'
        readyInMinutes = recipe.get('readyInMinutes')
        # readyInMinutes= '"' + readyInMinutes[1:-2] + '"'
        instructions = recipe.get('instructions').rstrip()
        # instructions = '"' + instructions[0:] + '"'
        ingredients_list = []
        ingredients = recipe.get('extendedIngredients')
        for ingredient in ingredients:
            ingredients_list.append(ingredient['original'])
        # ingredients = '"' + ingredients[1:-2] + '"'
        new_dict[f'recipe{i}'] = {
        
        "title" : title,
        "cuisine" : cuisine,
        "servings" : servings,
        "readyInMinutes" : readyInMinutes,
        "instructions" : instructions,
        "ingredients" : ingredients_list
        }
        i += 1 

    return new_dict

