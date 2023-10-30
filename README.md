This repo is home to the changes described in [this blog post](https://programmingmylife.com/2023-10-30-moving-from-django-microframework-to-django.html) written to explore some of the inner workings of Django by moving from the upstream Django Microframework to a more fully fledged blog project.

This is not intended to be merged back upstream. The original README is below.

# µDjango (Django as a Microframework)

How close can Django get to [Flask's](https://flask.palletsprojects.com/en/2.1.x/quickstart/) five-line "Hello, World!" implementation?

<img src="hello_world.png">

[Carlton Gibson](https://github.com/carltongibson) gave a talk at DjangoCon US 2019, [Using Django as a Micro-Framework](https://www.youtube.com/watch?v=w9cYEovduWI&list=PL2NFhrDSOxgXXUMIGOs8lNe2B-f4pXOX-&index=6&t=0s), where he demonstrated a single file implementation of "Hello, World!" in Django.

This repo demonstrates his original code example and subsequent attempts to display "Hello, World!" in a single file in as few lines of code as possible.

## Set Up

On the command line navigate to a directory, create and activate a new Python virtual environment, and install Django via `pip`.

```
# Windows
$ python -m venv .venv
$ .venv\Scripts\Activate.ps1
(.venv) $ python -m pip install django~=4.2.0

# macOS
$ python3 -m venv .venv
$ source .venv/bin/activate
(.venv) $ python -m pip install django~=4.2.0
```

## Option 1: [Carlton Gibson](https://github.com/carltongibson)

```python
# hello_django.py
from django.conf import settings
from django.core.handlers.wsgi import WSGIHandler
from django.http import HttpResponse
from django.urls import path

settings.configure(
    ROOT_URLCONF=__name__,
)

def hello_world(request):
    return HttpResponse("Hello, Django!")

urlpatterns = [
    path("", hello_world)
]

application = WSGIHandler()
```

Install [Gunicorn](https://gunicorn.org) to run the local server.

```
(.venv) $ python -m pip install gunicorn==21.2.0
```

Start the server.

```
(.venv) $ gunicorn hello_django:application
```

Navigate to [http://127.0.0.1:8000](http://127.0.0.1:8000). To stop the Gunicorn server, use `Ctrl+c` on the command line.

## Option 2: [Peter Baumgartner](https://github.com/ipmb) 
Peter offered an update using `execute_from_command_line` to make `python hello_django.py` the equivalent of running Django's `manage.py` command. It also does not need `Gunicorn` to be installed.

```python
# hello_django1.py
from django.conf import settings
from django.core.handlers.wsgi import WSGIHandler
from django.core.management import execute_from_command_line  # new
from django.http import HttpResponse
from django.urls import path

settings.configure(
    ROOT_URLCONF=__name__,
    DEBUG=True,  # new
)

def hello_world(request):
    return HttpResponse("Hello, Django!")

urlpatterns = [
    path("", hello_world)
]

application = WSGIHandler()

if __name__ == "__main__":  # new
    execute_from_command_line()
```

Then start the server with Django's `runserver` command.

```
(env) $ python hello_django1.py runserver
```

And navigate to [http://127.0.0.1:8000](http://127.0.0.1:8000). 
