# Pokécards - Pokémon Trading Card Collection Builder

## Description

Pokécards is a web application built with Django, Python, and JavaScript. It allows users to build and manage their Pokémon trading card collections online.

## Features

- User registration and authentication system.
- Browse and search Pokémon trading cards from a comprehensive database.
- Add cards to your collection and manage your collection.
- User-friendly interface for an enjoyable user experience.

## Installation

1. Clone the repository:

```
git clone https://github.com/Endeyr/pokecardsV2.git
```

2. Change into the project directory:

```
cd pokecardsV2
```

3. Create a virtual environment:

Install python3 and python3 venv if you haven't already

```
python3 -m venv env
```

1. Activate the virtual environment:

```
source env/bin/activate
```

5. Install the required dependencies:

```
pip install -r requirements/dev.txt
```

6. Set up env:

Follow the env_template

7. Add api key:

Sign up at https://dev.pokemontcg.io/
Add api key to secrets.py created in step 6

8. Set up the database:

```
python manage.py makemigrations
```

```
python manage.py migrate
```

9.  Setup tailwind:

```
python manage.py tailwind install
```

10. Run tailwind:

```
python manage.py tailwind start
```

10. Run the development server:

```
python manage.py runserver
```

11. Access the application by visiting http://localhost:8000 in your web browser.

## Usage

- Register a new account or log in with an existing account.
- Explore the collection of Pokémon trading cards.
- Add cards to your collection and manage your collection.
- Create a user bio.

## Contributing

I am not planning on updating or maintaining this project. If you would like to contribute please fork the repository.

## License

This project is licensed under the MIT License.

## Acknowledgements

This application uses data from the Pokémon TCG API. (Link to the API documentation)
Special thanks to the Django, Python, and TailwindCSS communities for their excellent frameworks and libraries.
Inspired by https://pokemontcg.guru/

## Project

This project is a web application capstone for the CS50's Web Programming course. It is for educational purposes only.
This project is not a social media or e-commerce site but built to utilize an api, explore and create databases, be mobile-responsive, and utilize django for the back-end and javascript for the front-end.

## Distinctiveness and Complexity

## File Explanations

These are the important files for the project and their usage:

# templates/base

The main html for this project. These files handle the front end for searching, creating collections, viewing user profile, navigation, and the base index. I created a html file for each page of functionality and decided to use tailwind to style my components as I wanted a mobile first design pattern. Tailwind ended up being the best choice since it is by design mobile first.

# templates/users

The user html for this project. These files handle the front end for user registration and login functionality. I utilized django's builtin user creation and authentication then created these files as the font end. Again I used tailwind along with django's form model.

# templates/registration

# templates/core

# assets/index.js

# assets/search.js

# core/admin

# core/forms

# core/models

# core/views

# core/urls

# urls.py

# views.py

# pokecardsV2/conf

# pokecardsV2/wsgi

# pokecardsV2/context_processor

# theme/static_src/tailwind.config.js

# users/forms

# users/urls

# users/views

# users/models

# requirements

# manage.py

# webpack.config.js

## Additional Information
