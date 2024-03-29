import os
import json
from random import choice, randint
import api_call

import crud
import model
import server

with server.app.app_context():

    os.system('dropdb fmoody')
    os.system('createdb fmoody')

    model.connect_to_db(server.app)
    model.db.create_all()

    with open("data/cuisines_playlist_data.json") as f:
        cuisine_data = json.loads(f.read())

    recipes_in_db = []
    for cuisine_playlist in cuisine_data:
        cuisine = cuisine_playlist.get('name').lower()
        recipes = api_call.api_call(cuisine)
        print(recipes)
        playlist = cuisine_playlist.get('playlist_id')

        for recipe in recipes:
            title, image, cuisine, servings, readyInMinutes, ingredients, instructions = (
                recipes[recipe].get('title'),
                recipes[recipe].get('image'),
                recipes[recipe].get('cuisine'),
                recipes[recipe].get('servings'),
                recipes[recipe].get('readyInMinutes'),
                recipes[recipe].get('ingredients'),
                recipes[recipe].get('instructions')
            )
            db_recipe = crud.create_recipe(
                title, image, cuisine, servings, readyInMinutes, ingredients, instructions, playlist)
            recipes_in_db.append(db_recipe)

        cuisines_in_db = []
        for cuisine in cuisine_data:
            name, playlist_id = (
                cuisine["name"],
                cuisine["playlist_id"],
            )

            db_cuisine = crud.create_cuisine(name, playlist_id) 
            cuisines_in_db.append(db_cuisine)

    for n in range(10):
        user_name = f'User{n}'
        user_email = f"user{n}@test.com"  # Voila! A unique email!
        user_password = "test"
        user = crud.create_user(user_name, user_email, user_password)
        model.db.session.add(user)

        model.db.session.add_all(cuisines_in_db)
        model.db.session.add_all(recipes_in_db)
        model.db.session.commit()
