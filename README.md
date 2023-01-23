# FMOODY (MmMmmFoodie)


Music and Food bring pleasure to our mind, body, and spirit, creating a sense of connection and harmony with the physical world. Music and Food are an essential element of culture. Sharing music from one culture to another gives people an insight into another way of life. Sharing foods has lead to a more globalized and diverse diet. Music can unite people of various cultures forming valuable connections and strengthening unity.
This is even more crucial during times of conflict when other methods of interaction are rendered impractical.

"Music teaches children about their heritage, fosters language development, and present new values. Educating children about different cultures promotes socialization, tolerance, and openness. These characteristics can lead to an appreciation of diversity and assist in establishing new relationships."
   -Starbright Books "Engaging Children in Multicultural Music" - 2021

The vision of this project is to create a platform where these shared recipes and music from different cultures can come to explore each other.  I have found the most cultural education and understanding from experiencing a cultures food and music. MmMmmFoodie's mission is to bring the world together through diverse cultures bringing music and shared recipes! Bon Apetite! 

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
python3 server.py
Navigate to localhost:5000
```
## Contact 
* Robert Fraser: robert.fraser876@gmail.com
* LinkedIn: https://www.linkedin.com/in/robertfraser415
* Project Repo Link: https://github.com/RobertFraser415/fmoody.git
* Live Project Link:    //aws or heroku here <<<<<<<>>>>>>>//



## LEFTOVERS TO DO


   screen recording technologies of .gif   also embed .gifs
        # gif maker   


   Project Process Reflection
    Spoonacular API was difficult to even read with results from the api but after creating variables for the hard to get to information I was able to work with the data. Once I had finally started getting the correct data to print for me, I started an architecture that was primarily sending information through forms through my buttons. However the format of a string was unable to be transformed in the way I needed. This lead to an entire restructuring of the architecture half way through the project weeks. I was able to go back and redesign the data flow and by creating my own transformed objects into the types I needed I was able to finally reach my MVP. Styling was fun and I enjoyed working with the design tools from lecture and also exploring CSS. I would continue to build out a yelp and spotify component that played spotify on the way to a restaurant of a chosen cuisine.





