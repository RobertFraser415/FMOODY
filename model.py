from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def connect_to_db(app, db_name):
    """connect to Database"""
    app.config["SQLALCHEMY_DATABASE_URI"] = f"postgresql:///{'fmoody'}"
    app.config["SQLALCHEMY_ECHO"] = True
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    db.app = app
    db.init_app(app)

if __name__ == "__main__":
    from server import app

    connect_to_db(app, "fmoody")


class User(db.Model):
    """someone using the app"""

    __tablename__ = 'users'

    user_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_name = db.Column(db.String(100), nullable=False)
    user_email = db.Column(db.String(100), nullable=False, unique=True)
    user_password = db.Column(db.String(100), nullable=False)

    cuisine = db.relationship("Cuisine", back_populates="cuisines")
    playlist = db.relationship("Playlist", back_populates="playlists")

    def __repr__(self):
        return f'<User id={self.user_id} name={self.user_name} email={self.user_email} password={self.user_password}>'



class UserCuisine(db.Model):
    """a users selected cuisines"""

    __tablename__ = "user_cuisines"

    user_cuisine_id = db.Column(db.Integer, autoincremenr=True, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.user_id"), nullable=False)
    cuisine_id = db.Column(db.Integer, db.ForeignKey("cuisines.cuisine_id"), nullable=False)

    cuisines = db.relationship("Cuisine", back_populates="user_cuisines")
    users = db.relationship("User", back_populates="user_cuisines")

class Cuisine(db.Model):
    """A style of food from a region"""

    __tablename__ = 'cuisines'

    cuisine_id = db.Column(db.Integer, primary_key=True, autoincremement=True)
    cuisine_name = db.Column(db.String(30), nullable=False, unique=True)
    cuisine_description = db.Column(db.String(50), nullable=True)

    cuisine_recipes = db.relationship("CuisineRecipe", back_populates="cuisines")
    cuisine_playlist = db.relationship("CuisinePlaylist", back_populates="cuisines")



    def __repr__(self):
        return f'<Mood id={self.mood_id} name={self.mood_name}>'


class CuisinePLaylist(db.Model):
    "cuisine related playlist"

    __tablename__ = "cuisines_playlist"

    cuisines_playlist_id = db.Column(db.Integer, autoincremenr=True, primary_key=True)
    playlist_id = db.Column(db.Integer, db.ForeignKey("playlist.playlist_id"), nullable=False)
    cuisine_id = db.Column(db.Integer, db.ForeignKey("cuisines.cuisine_id"), nullable=False)

    cuisines = db.relationship("Cuisine", back_populates="cuisines_playlist")
    playlist = db.relationship("Playlist", back_populates="cuisines_playlist")

class Playlist(db.Model):
    """a list of songs from that region"""

    __tablename__ = 'playlists'

    playlist_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    playlist_title = db.Column(db.String(50), nullable=False,)

    cuisine_playlist = db.relationship("CuisinePlaylist", back_populates="playlists")


    def __repr__(self):
        return f'<Song id={self.song_id} title={self.song_title} artist={self.artist} genre={self.genre}>'


class Recipe(db.Model):
    """a recipe from fetch call"""
    __tablename__ = 'recipes'

    recipe_id = db.Column(db.Integer, autoincremenr=True, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    ingredients = db.Column(db.String(1000), nullable=False)
    directions = db.Column(db.String(1000), nullable=False)

    cuisine_recipes = db.relationship("CuisineRecipe", back_populates="recipes")

class CuisineRecipe(db.Model):
    """a recipe from the cuisine selection"""

    __tablename__ = 'cuisine_recipes'

    cuisine_recipe_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    cuisine_id = db.Column(db.Integer, db.ForeignKey("cuisines.cuisine_id"), nullable=False)
    recipe_id = db.Column(db.Integer, db.ForeignKey("recipes.recipe_id"), nullable=False)

    cuisines = db.relationship("Cuisine", back_populates="cuisine_recipes")
    recipes = db.relationship("Recipe", back_populates="cuisine_recipes")