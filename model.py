from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

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

class Mood(db.Model):
    """A Current Feeling or Mood"""

    __tablename__ = 'moods'

    mood_id = db.Column(db.Integer, primary_key=True, autoincremement=True)
    mood_name = db.Column(db.String(30), nullable=False, unique=True)
    mood_description = db.Column(db.String(50), nullable=True)

    def __repr__(self):
        return f'<Mood id={self.mood_id} name={self.mood_name}>'

class Song(db.Model):
    """a peice of music"""

    __tablename__ = 'songs'

    song_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    song_title = db.Column(db.String(50), nullable=False,)
    artist = db.Column(db.String(50), nullable=False,)
    genre = db.Column(db.String(50), nullable=False,)

    def __repr__(self):
        return f'<Song id={self.song_id} title={self.song_title} artist={self.artist} genre={self.genre}>'



class User(db.Model):
    """someone using the app"""

    __tablename__ = 'users'

    user_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_name = db.Column(db.String(50), nullable=False,)
    user_email = db.Column(db.String(50), nullable=False, unique=True,)
    user_password = db.Column(db.String(50) nullable=False)

    def __repr__(self):
        return f'<User id={self.user_id} name={self.user_name} email={self.user_email} password={self.user_password}>'
