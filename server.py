from flask import Flask, render_template, request, flash, session, redirect
from model import connect_to_db, db
import crud
import api_call
import json

from jinja2 import StrictUndefined

app = Flask(__name__)
app.secret_key = "dev"
app.jinja_env.undefined = StrictUndefined


@app.route("/")
def homepage():
    """View homepage."""
    #new account created flashes this message 
    flash("Welcome! You can now log in!")
#  view homepage with login and a try as a guest  button ! 
    return render_template("homepage.html")



@app.route('/results')
def view_results(): 
    """View 3 recipes to choose from ."""
# mkae a api call return  a jinija tamplate with 3 results
    
    recipes = api_call.api_call('mexican')
    return render_template("results.html", recipes=recipes)


@app.route("/recipe_player", methods=['GET', 'POST'])
def show_recipe_playlist():
    """Show a full recipe next to the music player """
    recipe = request.form["recipe"]
    # recipe = request.json()
    # recipe = dict(recipe)
    # using json.loads() method
    result = json.loads(json.dumps(recipe))
    # print('\n\n\n\n\n')
    # print(recipe)
    # print(result)
    # print(type(result))
    # print('\n\n\n\n\n')

    print(type(recipe))
    title = recipe.get("title")
    # id = "recipe"  
    # name="recipe"
    # recipe= request.form[value]
    print(title)
    # playlist = crud. Crete function for getting playlist from data file (movie_id)
    # recipe = crud.   get recipe from results
    return render_template("recipe_player.html", playlist='playlist')



@app.route("/save_recipe", methods=["POST"])
def save_recipe():
    """saves a favorite recipe to view on the favorites page """
    # favorite = Favorite()  create a saved recipe  in database
    # need to check if user has already saved this previously no doubles
    # return will be  a message saying saved successfulyy 


@app.route("/select", methods=["POST"])
def choose_cuisine():
    """shows cuisine buttons and random to selct and take user to results """

    return render_template('select_page.html')

@app.route("/users", methods=["POST"])
def register_user():
    """Create a new user."""

    email = request.form.get("email")
    password = request.form.get("password")

    user = crud.get_user_by_email(email)
    if user:
        flash("Cannot create an account with that email. Try again.")
    else:
        user = crud.create_user(email, password)
        db.session.add(user)
        db.session.commit()
        flash("Account created! Please log in.")

    return redirect("/")


@app.route("/saved_favorites")
def show_favorites(user_id):
    """Show  a users saved favorites."""

    email = session.get("user_email")


    # create a remove button 
    # if logged in , render template else
    if email:
        return render_template("favorites.html", email=email, favorites=favorites)
    else: 
        return render_template("make_one.html")



@app.route("/make_one")
def show_unlogged():
    """Shows a  user the message MAke An Account ."""

    return render_template("make_one.html")


@app.route("/login", methods=["POST"])
def process_login():
    """Process user login."""

    email = request.form.get("email")
    password = request.form.get("password")

    user = crud.get_user_by_email(email)
    if not user or user.password != password:
        flash("The email or password you entered was incorrect.")
    else:
        # Log in user by storing the user's email in session
        session["user_email"] = user.email
        flash(f"Welcome back, {user.email}!")

    return redirect("/")

# @app.route("/remove favorite", methods=["POST"])
# def remove_favorite():
#     rating_id = request.json["rating_id"]
#     updated_score = request.json["updated_score"]
#     crud.update_rating(rating_id, updated_score)
#     db.session.commit()

#     return "Success"

# @app.route("/movies/<movie_id>/ratings", methods=["POST"])
# def create_rating(movie_id):
#     """Create a new rating for the movie."""

#     logged_in_email = session.get("user_email")
#     rating_score = request.form.get("rating")

#     if logged_in_email is None:
#         flash("You must log in to save a favorite recipe.")
#     elif not rating_score:
#         flash("Error: you didn't select a score for your rating.")
#     else:
#         user = crud.get_user_by_email(logged_in_email)
#         movie = crud.get_movie_by_id(movie_id)

#         rating = crud.create_rating(user, movie, int(rating_score))
#         db.session.add(rating)
#         db.session.commit()

#         flash(f"You rated this movie {rating_score} out of 5.")

#     return redirect(f"/movies/{movie_id}")


if __name__ == "__main__":
    connect_to_db(app)
    app.run(host="0.0.0.0", debug=True)

