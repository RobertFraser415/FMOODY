# FMOODY
   project description 

   tech stack
Spotify 
Spoonacular 
   Flask
   Flask SQLAlchemy 
   Jinja 2
   Bootstrap
   HTML
   CSS

  Highlighted Features: 
    1 - A user can select a cuisine to explore
    
    2 - A user can then recieve some random recipes to choose from.

    3 - Then a user is populated the recipe information and a player from spotify with a playlist that corresponds to the tradional music from that cuisines region.

    4 - Users can create an account with an email and password or search for recipes as a guest. 
    
    5 - Registered users can save their favorites.

    6 - Registered users can create a recipe to add to the database.

    Screenshots:
    
![Alt text](/Users/robertfraser/Desktop/1 fmoody.png?raw=true "Optional Title")
   

 
   


    

  

   screen recording technologies of .gif   also embed .gifs
        # gif makeer   
    how to install    requirmtents .txt etc 

    markdown cheet sheet 
    push to git hub it is homepage fo repo


    customize pinned repositories 

    make project public 

    

    MmMmmFoodie 
@@@Description    VISION MISSION

Technology Stack
Backend: Python, SQLAlchemy, Jinja, Flask
Frontend: HTML, CSS, Bootstrap, JavaScript
Database: PostgreSQL
API's: 

MmMmmFoodie is deployed, but here is how to run the app locally:

Clone the repository:

git clone https://github.com/RobertFraser415/fmoody.git
Prerequisites:

Python3
PostgreSQL
Set up and activate a virtual environment, install dependencies:

cd Project
pip3 install virtualenv
virtualenv env
source env/bin/activate
pip3 install -r requirements.txt

Setting up the database:
python3 seed_database.py

Obtaining and using API Keys:

Spoonacular API: request a key at https://https://spoonacular.com/food-api
Save API key in a secret shell file labeled "secrets.sh"
The text of that file should be:

export API_KEY = YOUR_API_KEY_HERE_000

Add this file to your .gitignore if you wish.

Running the application:
python3 flask_app.py
Navigate to localhost:5000