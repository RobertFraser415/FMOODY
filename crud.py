"CRUD functionality"

from model import db, User, Recipe , Cuisine, Favorite, connect_to_db

def create_user(name, email, password):
    """Create and return a new user."""

    user = User(name=name, email=email, password=password)

    return user

def create_cuisine(name, playlist_id):
    cuisine = Cuisine(name=name, playlist_id=playlist_id)
    return cuisine


def create_recipe(title , servings, readyInMinutes, original, instructions):
    recipe = Recipe(title=title, servings=servings, readyInMinutes=readyInMinutes, original=original, instructions=instructions)
    return recipe


def create_favorite(user_id, recipe_id):
    favorite = Favorite(user_id=user_id, recipe_id=recipe_id)
    return favorite


if __name__ == '__main__':
    from server import app
    connect_to_db(app)