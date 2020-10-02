# Cloth Store

A simple cloth store system using Python Django framework and MySQL database. Included trending and simple recommendation feature.

### Installation

Install python environment to run. (Minimum python version is >= Python 3.6)

```sh
$ python3.6 -m venv devEnv
```

Run python virtual environment and install dependencies

```sh
$ source devEnv/bin/activate
$ pip install -r requirements.txt
```

Go to project folder where the manage.py file located and migrate database model, and run on your local system

```sh
$ python manage.py migrate
$ python manage.py runserver
```
