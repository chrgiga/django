# **My first practices with Django**

Author: Christian Gil

**Description:**

This project consist in a simple questionary form, that provides users with a health status diagnosis 
according to the indicated symptoms.

## **Set up**

This project based in Django framework works with a Postgresql database.
Assume that we have installed and well configured the server and database.

- Make migrations:

    The project has 2 models inside **main** folder, **Question** and **Symptom**.
    We need to create the correspondent tables on database, for that execute the follow commands:
    
    `python manage.py makemigrations main`
    
    `python manage.py migrate`
   
- Populate database with some default values:

    We have prepared some fixtures for corresponding models, for populate database 
    execute the follow commands:
    
    `python manage.py loaddata symptoms`
    
    `python manage.py loaddata questions`

- Run project in your browser:
    
    Visit the homepage with your server url (in my case is http://localhost:8000)
    
    If everything goes fine you can see a welcome title and link to the questionary
