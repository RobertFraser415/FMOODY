import os
import json
from random import choice, randint
from datetime import datetime

import crud
import model
import server

with server.app.app_context():

    os.system('dropdb fmoody')
    os.system('createdb fmoody')

    model.connect_to_db(server.app, 'fmoody')
    model.db.create_all()

    with open("data/recipes_response.json") as f:
        recipe_data = json.loads(f.read())

    with open("data/cuisines_playlist_data.json") as f:
        cuisine_data = json.loads(f.read())

    # with open("data/users_list.json") as f:
    #     user_data = json.loads(f.read())

    # Create movies, store them in list so we can use them
    # to create fake ratings
    recipes_in_db = []
    recipes = recipe_data['recipes']
    for recipe in recipes:
        title, servings, readyInMinutes, original, instructions = (
            recipe["title"],
            recipe["servings"],
            recipe["readyInMinutes"],
            recipe["original"],
            recipe["instructions"],
        )
        print(original)
        db_recipe = crud.create_recipe(title, servings, readyInMinutes, original, instructions)
        recipes_in_db.append(db_recipe)


    # users_in_db = []
    # for user in user_data:
    #     name, email, password = (
    #         recipe["name"],
    #         recipe["email"],
    #         recipe["password"],
    #     )
    #     date_added = datetime.strptime(user["date_added"], "%Y-%m-%d")

    #     db_recipe = crud.create_recipe(title, servings, readyInMinutes, ingredients, instructions)
    #     recipes_in_db.append(db_recipe)

    cuisines_in_db = []
    for cuisine in cuisine_data:
        name, playlist_id = (
            cuisine["name"],
            cuisine["playlist_id"],
        )

        db_cuisine = crud.create_cuisine(name, playlist_id)
        cuisines_in_db.append(db_cuisine)

    for n in range(10):
        email = f"user{n}@test.com"  # Voila! A unique email!
        password = "test"

        user = crud.create_user(email, password)
        model.db.session.add(user)

        # for _ in range(10):
        #     random_movie = choice(movies_in_db)
        #     score = randint(1, 5)

        #     rating = crud.create_rating(user, random_movie, score)
        #     model.db.session.add(rating)


    model.db.session.add_all(recipes_in_db)
    model.db.session.add_all(cuisines_in_db)
    # model.db.session.add_all(users_in_db)
    model.db.session.commit()

    # Create 10 users; each user will make 10 ratings

    model.db.session.commit()