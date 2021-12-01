# Urlshortener_django
An application that generates a shorter URL using Python-Django. Hosted this application on Heroku.

```
To run the Urlshortener_django app in your local system

Fork or download this repository on your system.

You need to do some changes in the listed folder or file mentioned below:
1.	Django_Urlshortenet
a.	Settings.py file
Comment line number 15 and 16
i.e.15.  import django_heroku
     16.  import dj_database_url
Comment line from 79 to 81  i.e.
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

Commnet line number 126
Django.heroku.settings(locals())

2.	Static folder 
a.	Js sub_folder
Script.js - file remove “www.urlshortenerdjango.tk/”  or comment this line 13.

$('h2').html("www.urlshortenerdjango.tk/"+data)
Add below line
            $('h2').html("localhost:8000/"+data)
```
