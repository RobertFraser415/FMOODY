# FMOODY (MmMmmFoodie)

description vision mission 

## Highlighted Features:
* A user can select a cuisine to explore
    
* A user can then recieve some random recipes to choose from.

* Then a user is populated the recipe information and a player from spotify with a playlist that corresponds to the tradional music from that cuisines region.

* Users can create an account with an email and password or search for recipes as a guest. 
    
* Registered users can save their favorites.

* Registered users can create a recipe to add to the datab

## Technology Stack
   * **Backend:** Python, SQLAlchemy, Jinja2, Flask
   * **Frontend:** HTML5, CSS3, Bootstrap5, JavaScript
   * **Database:** PostgreSQL
   * **API's:** Spoonacular

## Screenshots:

screenshots  here <><><><><><>


## Installation

MmMmmFoodie is deployed, but here is how to run the app locally:

Clone the repository:

```
git clone https://github.com/RobertFraser415/fmoody.git
```

Prerequisites:
* Python3
* PostgreSQL

Set up and activate a virtual environment, install dependencies:
```
cd Project
pip3 install virtualenv
virtualenv env
source env/bin/activate
pip3 install -r requirements.txt
```
Setting up the database:

```
python3 seed_database.py
```

Obtaining and using API Keys:
* Spoonacular API: request a key at https://https://spoonacular.com/food-api
* Save API key in a secret shell file labeled "secrets.sh"
* The text of that file should be:
* export API_KEY = YOUR_API_KEY_HERE_000
* Add to your .gitignore if you wish.

Running the application:
```
python3 flask_app.py
Navigate to localhost:5000
```
## Contact 
* Robert Fraser: robert.fraser876@gmail.com
* LinkedIn: https://www.linkedin.com/in/robertfraser415
* Project Repo Link: https://github.com/RobertFraser415/fmoody.git
* Live Project Link:    //aws or heroku here <<<<<<<>>>>>>>//



## LEFTOVERS TO DO


   screen recording technologies of .gif   also embed .gifs
        # gif makeer   


   difficulties 
    Spoonacular API was difficult to even read with results from the api but after creating variables for the hard to get to information I was able to work with the data. Once I had finally started getting the correct data to print for me, I started an architecture that was primarily sending information through forms through my buttons. However the format of a string was unable to be transformed in the way I needed. This lead to an entire restructuring of the architecture half way through the project weeks. I was able to go back and redesign the data flow and by creating my own transformed objects into the types I needed I was able to finally reach my MVP. Styling was fun and I enjoyed working with the design tools from lecture and also exploring CSS.





