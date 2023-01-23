from flask import Flask, render_template, request, flash, session, redirect, jsonify
from model import connect_to_db, db, User
import crud
import api_call
import json
import re


from jinja2 import StrictUndefined

app = Flask(__name__)
app.secret_key = "dev"
app.jinja_env.undefined = StrictUndefined


@app.route("/", methods=["GET", "POST"])
def homepage():
    """View homepage."""
    # new account created flashes this message
    flash("Welcome! You can now log in!")
#  view homepage with login and a try as a guest  button !
    return render_template("homepage.html", email=session.get('user_email'))


@app.route('/results')
def view_results():
    """View 3 recipes to choose from ."""
# mkae a api call return  a jinija tamplate with 3 results
# need to pull argument from form here as cuisine   vvvv
    if 'user_email' in session:
        email = session['user_email']
    else:
        email = None
    cuisine = request.args.get("cuisine_selection")
    print(cuisine)
    res = api_call.api_call(cuisine)
    recipes = []
    print(res)
    for key in res.keys():
        recipe = res[key]
        recipes.append({
            "title": recipe['title'],
            "image": recipe['image'],
            "cuisine": recipe['cuisine'],
            "servings": recipe['servings'],
            "readyInMinutes": recipe['readyInMinutes'],
            "ingredients": recipe['ingredients'],
            "instructions": recipe['instructions']})
    return render_template("results.html", recipes=recipes, email=email)


@app.route("/recipe_player", methods=['GET', 'POST'])
def show_recipe_playlist():
    if 'user_email' in session:
        email = session['user_email']
    else:
        email = None
        
    user = crud.get_user_by_email(email)
    if user: 
        favorites = user.favorites
    else: favorites = None

    """Show a full recipe next to the music player """
    recipe_str = request.form["recipe"]

    recipe = crud.query_recipe(recipe_str)
    # /string stuff
    # print(recipe.ingredients)
    # string_ingredients = recipe.ingredients.strip("{").strip("}").strip(' " ').split(",")
    
    
    string_ingredients = recipe.ingredients
    clean_ingredients = re.sub("[^a-zA-Z//\d/,g\s]+", "",string_ingredients)
    print(clean_ingredients)
    split_ingredients = clean_ingredients.split(",")
    final_ingredients = [ing.strip() for ing in split_ingredients]
    for ing in final_ingredients:
        print("-", ing)

    
    # print(string_ingredients[0],",", string_ingredients[1])
    # print(json.loads(string_ingredients))

    # for i in just_quotes:

    # recipe.split() => [“1/2 cornmeal”, “1/2 teaspoon salt”...]
    # loop over split list  
    # make it a list if commas and } in sting remove carly
    # jinja template for loop for bulletpoints 

    # playlist = recipe.playlist_id
    # print(playlist)

    return render_template("recipe_player.html", recipe=recipe, email=email, favorites=favorites,  ingredients=final_ingredients) 


@app.route("/save_recipe", methods=['POST'])
def save_recipe():
    """saves a favorite recipe to view on the favorites page """
    flash('Recipe was successfully saved to your favorites! YAY!!')
    # favorite = Favorite()  create a saved recipe  in database
    # need to check if user has already saved this previously no doubles
    # return will be  a message saying saved successfulyy
    if 'user_email' in session:
        user = crud.get_user_by_email(session['user_email'])
        user_id = user.user_id
        # print('\n\n\n',user_id, '\n\n\n')
        recipe_id = request.form.get('recipe')
        print(recipe_id)
        print(request.form)
        print('***********************************************', user_id, recipe_id)
        
        favorite = crud.create_favorite(user_id, recipe_id)
        if favorite not in db.session:
            db.session.add(favorite)
            db.session.commit()
        
        print(f' FAVORITE =========== = {favorite}')
        favorites = crud.get_user_favorites(user_id)
        print(f'%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%{favorites}')
        return render_template('favorites.html', favorites=favorites)
    else:
        return redirect('/make_one')

@app.route("/select", methods=["POST"])
def choose_cuisine():
    """shows cuisine buttons and random to selct and take user to results """

    return render_template('results.html')


@app.route("/users", methods=["POST"])
def register_user():
    """Create a new user."""

    name = request.form.get("name")

    email = request.form.get("email")
    password = request.form.get("password")
    print(name, email, password, '################################')
    user = crud.get_user_by_email(email)
    if user:
        flash("Cannot create an account. This email already exsist. Try again.")
    else:
        user = crud.create_user(name, email, password)
        db.session.add(user)
        db.session.commit()
        flash("Account created! You are logged in.")

    return redirect("/")


@app.route("/favorites")
def show_favorites():
    """Show  a users saved favorites."""

    email = session.get("user_email")

    # create a remove button
    # if logged in , render template favorite else not logged in route to make one
    if email:
        current_user = crud.get_user_by_email(email)
        favorites = current_user.favorites
        print(f'favorites {favorites}')
        # print(f'favorites {favorites.recipe}')
        return render_template("favorites.html", email=email, favorites=favorites)
    else:
        return render_template("make_one.html")


@app.route("/make_one")
def show_unlogged():
    """Shows a  user the message MAke An Account ."""

    return render_template("make_one.html")


@app.route("/login", methods=["GET", "POST"])
def process_login():
    """Process user login."""
    if request.method == 'POST':
        email = request.form.get("user_email")
        password = request.form.get("user_password")
        user = crud.get_user_by_email(email)

        if not user or user.user_password != password:
            flash("The email or password you entered was incorrect.")
            return redirect('/login')#, email=session.get('user_email')
        else:
            # Log in user by storing the user's email in session
            session["user_email"] = user.user_email
            print('logged_in')
            email = session.get('user_email')
            favorites = user.favorites
            print(email)
            flash(f"Welcome back, {user.user_name}!")
            print(f'###############################{favorites}')
            return render_template('favorites.html', email=email, favorites=favorites)
    
    return render_template('login.html')
    # , email=session.get('user_email')


@app.route("/logout")
def logout():
    flash('YOU HAVE SUCCESSFULLY LOGGED OUT ')
    session.pop('user_email', None)
    return redirect('/')


# @app.route("/add_favorite/{recipe_id}")
# def add_fav(recipe_id):
#     user_email = session.get('email')
#     user = crud.get_user_by_email(user_email)
#     # recipe_id = request.form.get('recipe')
#     print("!!!!!!!!!!!!!!!!!!!!!!!")
#     print(recipe_id)
#     favorite = crud.create_favorite(user.user_id, recipe_id)
#     db.session.add(favorite)
#     db.session.commit()
#     # return redirect('/favorites')
#     return render_template('favorites.html', favorite=favorite)


@app.route("/add_recipe", methods=['POST'])
def add_recipe():
    # """saves a favorite recipe to view on the favorites page """
    """saves a recipe to the database then redirect to favorites page """
        # favorite = Favorite()  create a saved recipe  in database
    # need to check if user has already saved this previously no doubles
    # return will be  a message saying saved successfulyy
    if 'user_email' in session:
        user = crud.get_user_by_email(session['user_email'])
        user_id = user.user_id
        # recipe_id = recipe.recipe_id
        title = request.form.get("title-form")
        image = request.form.get("image-form")
        cuisine = request.form.get("cuisine-form")
        servings = request.form.get("servings-form")
        readyInMinutes = request.form.get("readyInMinutes-form")
        ingredients = request.form.get("ingredients-form")
        instructions = request.form.get("instructions-form")

        recipe_id = request.form.get('recipe')
        print(request.form)
        # print('***********************************************', user_id, recipe_id)
        
        recipe_to_add = crud.create_recipe(title, image, cuisine, servings, readyInMinutes, ingredients, instructions, playlist='37i9dQZF1DX4UtSsGT1Sbe')
        if recipe_to_add not in db.session:
            db.session.add(recipe_to_add)
            db.session.commit()
        # crud.create_favorite(user_id, recipe.recipe_id)
            
        added_recipe = crud.create_favorite(user_id, recipe_to_add.recipe_id)
        if added_recipe not in db.session:
            db.session.add(added_recipe)
            db.session.commit()
            favorites = crud.get_user_favorites(user_id)
            print(f'%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%{favorites}')
        return render_template('favorites.html', favorites=favorites)
    else:
        return redirect('/make_one')


if __name__ == "__main__":
    connect_to_db(app)
    app.run(host="0.0.0.0", debug=True)
