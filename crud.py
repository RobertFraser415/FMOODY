"CRUD functionality"

from model import db, User, Recipe , Cuisine, Favorite, connect_to_db

def create_user(user_name, user_email, user_password):
    """Create and return a new user."""

    user = User(user_name=user_name, user_email=user_email, user_password=user_password)

    return user

def create_cuisine(name, playlist_id):
    cuisine = Cuisine(name=name, playlist_id=playlist_id)
    return cuisine


def create_recipe(title, cuisine, servings, readyInMinutes, ingredients, instructions, playlist):
    recipe = Recipe(title=title, cuisine=cuisine, servings=servings, readyInMinutes=readyInMinutes, ingredients=ingredients, instructions=instructions, playlist=playlist)
    return recipe


def create_favorite(user_id, recipe_id):
    favorite = Favorite(user_id=user_id, recipe_id=recipe_id)
    return favorite


def query_cuisine(name):
    return Cuisine.query.filter_by(name=name).first()

def query_recipe(title):
    return Recipe.query.filter_by(title=title).first()

def get_user_by_email(user_email):
    return User.query.filter_by(user_email=user_email).first()



if __name__ == '__main__':
    from server import app
    connect_to_db(app)