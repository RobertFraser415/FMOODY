from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    """someone using the app"""

    __tablename__ = 'users'

    user_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_name = db.Column(db.String(100), nullable=False)
    user_email = db.Column(db.String(100), nullable=False, unique=True)
    user_password = db.Column(db.String(100), nullable=False)
    
    favorites = db.relationship("Favorite", back_populates='user')
    user_recipes_ = db.relationship("UserRecipe", back_populates="users_")
    # playlist_ = db.relationship("Playlist", back_populates="playlists_")

    def __repr__(self):
        return f'<User id={self.user_id} name={self.user_name} email={self.user_email} password={self.user_password}>'



class UserRecipe(db.Model):
    """a users favorite recipes"""

    __tablename__ = "user_recipes"

    user_recipe_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.user_id"), nullable=False)
    recipe_id = db.Column(db.Integer, db.ForeignKey("recipes.recipe_id"), nullable=False)

    recipes_ = db.relationship("Recipe", back_populates="user_recipes_")
    users_ = db.relationship("User", back_populates="user_recipes_")

class Cuisine(db.Model):
    """A style of food from a region"""

    __tablename__ = 'cuisines'

    cuisine_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(30), nullable=False, unique=True)
    playlist_id = db.Column(db.String(50), nullable=True)

   

# class CuisinePlaylist(db.Model):
#     "cuisine related playlist"

#     __tablename__ = "cuisines_playlists"

#     cuisine_playlist_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
#     playlist_id = db.Column(db.Integer, db.ForeignKey("playlist.playlist_id"), nullable=False)
#     cuisine_id = db.Column(db.Integer, db.ForeignKey("cuisines.cuisine_id"), nullable=False)

#     cuisines_ = db.relationship("Cuisine", back_populates="cuisine_playlist_")
#     # playlists_ = db.relationship("Playlist", back_populates="cuisine_playlist_")

# class Playlist(db.Model):
    """a list of songs from that region"""

#     __tablename__ = 'playlists'

#     playlist_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
#     playlist_title = db.Column(db.String(50), nullable=False,)

#     cuisine_playlist_ = db.relationship("CuisinePlaylist", back_populates="playlists_")


class Recipe(db.Model):
    """a recipe from fetch call"""
    __tablename__ = 'recipes'

    recipe_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    servings = db.Column(db.Integer, nullable=False)
    readyInMinutes = db.Column(db.Integer, nullable=False)
    ingredients = db.Column(db.String(1000), nullable=False)
    instructions = db.Column(db.String(1000), nullable=False)

    user_recipes_ = db.relationship("UserRecipe", back_populates="recipes_")
    favorites = db.relationship("Favorite", back_populates='recipe')

#     cuisine_recipes_ = db.relationship("CuisineRecipe", back_populates="recipes_")

# class CuisineRecipe(db.Model):
#     """a recipe from the cuisine selection"""

#     __tablename__ = 'cuisine_recipes'

#     cuisine_recipe_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
#     cuisine_id = db.Column(db.Integer, db.ForeignKey("cuisines.cuisine_id"), nullable=False)
#     recipe_id = db.Column(db.Integer, db.ForeignKey("recipes.recipe_id"), nullable=False)

#     cuisines_ = db.relationship("Cuisine", back_populates="cuisine_recipes_")
#     recipes_ = db.relationship("Recipe", back_populates="cuisine_recipes_")

class Favorite(db.Model):
    __tablename__ = 'favorites'

    favorite_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.user_id"), nullable=False)
    recipe_id = db.Column(db.Integer, db.ForeignKey("recipes.recipe_id"), nullable=False)

    user = (db.relationship("User", back_populates='favorites'))
    recipe = (db.relationship("Recipe", back_populates='favorites'))

def connect_to_db(app, db_name):
    """connect to Database"""
    app.config["SQLALCHEMY_DATABASE_URI"] = f"postgresql:///{db_name}"
    app.config["SQLALCHEMY_ECHO"] = True
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    db.app = app
    db.init_app(app)

if __name__ == "__main__":
    from server import app

    connect_to_db(app, "fmoody")