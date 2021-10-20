# User Profile API

<hr/>

## Setup the Project

1. Install Python 3.6 or above

2. Create a virtualenv and activate it
    ```
    $ pip install virtualenv 
    $ virtualenv venv
    $ venv\Scripts\activate        # For Windows
    $ source venv/bin/activate     # For Linux
    ```

3. Install dependencies
    ```
    $ pip install -r requirements.txt
    ```

4. Run the following commands for Migration.
    ```
    $ cd ./UserProfileApp
    $ python manage.py makemigrations
    $ python manage.py migrate
    ```

<br/>

## Project Structure

```
UserProfileApp
│   manage.py
│
├───templates
│   └───admin
│           base_site.html
│
├───UserProfileAPI
│   │   admin.py
│   │   apps.py
│   │   models.py
│   │   serializers.py
│   │   tests.py
│   │   urls.py
│   │   views.py
│   │   __init__.py
│   │
│   └───templatetags
│           i18n_switcher.py
│
└───UserProfileApp
        asgi.py
        middleware.py
        settings.py
        urls.py
        wsgi.py
        __init__.py
```

<br/>

## Run the Project

Run the following command

```
$ python manage.py runserver
```

You can use the Postman Collection present in the root directory of the project.
<br/><br/>

## Test APIs

Run the following command

```
$ python manage.py test
```

<br/>