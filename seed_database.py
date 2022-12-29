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

    for cuisine_playlist in cuisine_data:
        cuisine = cuisine_playlist.get('name').lower()
        recipes = api_call.api_call(cuisine)
        playlist = cuisine_playlist.get('playlist_id')
        recipes_in_db = []

        for recipe in recipes:
            title, cuisine, servings, readyInMinutes, original, instructions = (
                recipes[recipe].get('title'),
                recipes[recipe].get('cuisine'),
                recipes[recipe].get('servings'),
                recipes[recipe].get('readyInMinutes'),
                recipes[recipe].get('original'),
                recipes[recipe].get('instructions')
            )

            db_recipe = crud.create_recipe(
                title, cuisine, servings, readyInMinutes, original, instructions, playlist)
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
            name = f'User{n}'
            email = f"user{n}@test.com"  # Voila! A unique email!
            password = "test"
            user = crud.create_user(name, email, password)
            model.db.session.add(user)

        model.db.session.add_all(cuisines_in_db)
        model.db.session.add_all(recipes_in_db)
        model.db.session.commit()
