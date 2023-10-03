# Pokécards - Pokémon Trading Card Collection Builder

## Description

Pokécards is a web application built with Django, Python, and JavaScript. It allows users to build and manage their Pokémon trading card collections online.

Find the live version at: https://pokecards.onrender.com/

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

This project is distinct from social media and e-commerce sites. It is a card collection builder and does not have any social media or shopping features. As for complexity, it utilizes a wide range of django and javascript functionality, ranging from class based views, api access from both javascript and python, settings for production and development, and more. This project pushed me to learn how to setup a production environment, file structure, class based views, working with 3rd party applications such as aws s3 buckets and sendgrid, and more.

## File Explanations

These are the important files for the project and their usage:

# templates/base

The layout html, this holds the nav header and the footer to display on each page using {% extends %}.

# templates/users

The user html, these files handle the front end for user registration and login functionality. I utilized django's builtin user creation and authentication then created these files as the font end. Again I used tailwind along with django's form model.

# templates/registration

The registration html, I extended the default django class based registration views to better fit my project.

# templates/core

The main html, each page html is in this directory. I wanted a different page for search, collection viewing, card details, and forms.

# assets/index.js

Javascript for mobile menu responsiveness.

# assets/search.js

Main javascript for the project, centered around responsiveness for the search functionality. This file controls interaction with the pokemontcg api and displaying that information on the screen.

# core/admin

Allows the admin to add/remove from each model as well as view the data.

# core/forms

The forms for creating a collection or contacting me. These use the basic django form models.

# core/models

The card, collection and contact models for the project. I wanted each user to be able to create multiple collections to store their cards, and created a card model to have faster response on viewing cards ie not waiting for them to load from the api response.

# core/views

The main views for the project. I used multiple django class based views and mixins that suited each pages needs. Detail view on pages that passed one object, list view for multiple objects such as the collections page, and template or form view for the others.

# core/urls

The main url directory, I wanted each part of the application to have their own webpage. I also used the urls to pass information such as primary keys to other webpages.

# pokecardsV2/conf

The projects settings for development, staging, and production, as well as a common that shares between all three. This allowed me to develop the project locally then change specific settings to work with aws s3 bucket, sendgrid, render, and postgresql. It helped with finding bugs when I could change settings in one file then switch between to find the cause.

# pokecardsV2/wsgi

This file tells django what settings file to use, as I had a settings file changed from default I needed to update this.

# pokecardsV2/context_processor.py

The configuration file for passing information to each web page. I used this to pass my contact information and github to the footer and contact page.

# pokecardsV2/storage_backends.py

The configuration file for using aws s3 buckets to store my static files for web hosting. This allows me to have private and public files, if I wanted to add a user having private profile pictures or other files.

# theme/static_src/tailwind.config.js

I used tailwind for my css, this file allowed me to update in real time my style changes by running python manage.py tailwind start.

# users/forms

I extended the django forms to better fit my project. This included styling and adding placeholders as well as customizing the messages.

# users/urls

The url directory for the project user side.

# users/views

I extended the django views for logging in and out, as well as password changes and resets to fit my project. I needed to do this to customize the css as well as add redirects and messages.

# users/models

I extended the user model to add a profile to each user. This allowed me to add a bio and profile picture to each.

# requirements

Pip install requirements/dev.txt to install the python packages I used for this project. I setup the files to allow for different python packages for production and stage as well but didn't end up using them.

# manage.py, manage.stage.py, manage.prod.py

Django files to run the app. I used manage.py during development, manage.stage.py to test the production settings locally, and manage.prod.py for the deployed version. Each uses the corresponding wsgi and config files.

# webpack.config.js

Bundler setup for my javascript, let me update the page in real time with npm run dev.

## Additional Information

This project is my submission for the CS50's Web Programming with Python and JavaScript Capstone. I enjoyed working on this project and learned more about django, python, javascript, and web development than I would have otherwise. While not perfect, I think this project is a great reflection of where I am as a developer and shows that I am working hard towards improving. If you've read this far, thank you.
