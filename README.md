# Urlshortener_django
An application that generates a shorter URL using Python-Django. Hosted this application on Heroku.

# Result Images
![Main__page](https://user-images.githubusercontent.com/24228300/144216986-3b086ca1-8891-4686-86d7-1c7c49b9d7aa.PNG)
![Results_page](https://user-images.githubusercontent.com/24228300/144216996-7a1705fe-df88-4de2-8734-2d91dd76e8a7.PNG)

```
To run the Urlshortener_django app in your local system

Fork or download this repository on your system.

You need to do some changes in the listed folder or file mentioned below:

#1. Django_Urlshortenet
    # a. Settings.py file
    
#Comment line number 15 and 16 i.e.
    15.  import django_heroku
    16.  import dj_database_url
    
#Comment line from 79 to 81  i.e.
DATABASES = {
    'default': dj_database_url.config()
}

Add below content there:
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

#Commnet line number 126 i.e.
Django.heroku.settings(locals())

#2. Static folder 
     #a. Js sub_folder
     
Script.js - file remove “www.urlshortenerdjango.tk/”  or comment this line 13 i.e.
$('h2').html("www.urlshortenerdjango.tk/"+data)

Add below line
            $('h2').html("localhost:8000/"+data)
```
