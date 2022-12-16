import requests


def api_call(cuisine):
    payload = {'apiKey':'3888fcd00cc145eda0180b67fc4dd822',
    'number': 3,
    'tags':cuisine}

    search = requests.get('https://api.spoonacular.com/recipes/random?number=3lw', params=payload)

    results = search.json() 
    recipe = results.get('recipes')
    title = recipe[0].get('title')
    servings = recipe[0].get('servings')
    readyInMinutes = recipe[0].get('readyInMinutes')
    ingredients = recipe[0].get('extendedIngredients')
    instructions = recipe[0].get('instructions')

    print(title)
    print(servings)
    print(readyInMinutes)

    for ingredient in ingredients:
        # original = ingredient.get(original)
        # print(f'original={original}')
        print(ingredient['original'])

    print(instructions)


api_call('chinese')

