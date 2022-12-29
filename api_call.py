import requests
import json

# with open("data/cuisines_playlist_data.json") as f:
#     cuisine_data = json.loads(f.read())

# 


def api_call(cuisine):
    # payload = {'apiKey':'3888fcd00cc145eda0180b67fc4dd822',
    payload = {'apiKey':'ede5e343794c4af684778c4403cd197c',
    'number': 3,
    'tags': cuisine}
    print(cuisine)

    search = requests.get('https://api.spoonacular.com/recipes/random', params=payload)

    results = search.json() 
    print(results)
    
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
        instructions = recipe.get('instructions')
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
    # print(cuisine)
    # print(new_dict)
    return new_dict


# api_call('african')


# for cuisine_playlist in cuisine_data:
#     cuisine = cuisine_playlist.get('name').lower()
#     print(type(cuisine))
#     api_call(cuisine)
#     # print(recipes)

