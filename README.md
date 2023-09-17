# KU Polls
[![Python application](https://github.com/mjrchy/ku-polls/actions/workflows/python-app.yml/badge.svg)](https://github.com/mjrchy/ku-polls/actions/workflows/python-app.yml)

This app helps create surveys with multiple-choice questions specifically for Kasetsart University. It's made by following the [Django Tutorial project](https://docs.djangoproject.com/en/3.1/intro/tutorial01/) and includes extra features. 

A polls application for [Individual Software Process](https://cpske.github.io/ISP) course at [Kasetsart University](https://ku.ac.th).

## Install and Configure the Application

1. Cloning the repository
   ```
git clone https://github.com/mjrchy/ku-polls.git
   ```
2. Access to the project directory
```
cd ku-polls
```
3. Create a Virtual Environment and install requirements.txt
```python -m venv venv
. venv\Scripts\activate
pip install requirements.txt
```
4. Set Up the Database
```python manage.py migrate```
5. Download data
```
python manage.py loaddata data/users.json
python manage.py loaddata data/polls.json
```
6. Run the server
```
python manage.py runserver
```

## Project Documents

All project-related documents are in the [Project Wiki](../../wiki/Home)

- [Vision Statement](../../wiki/Vision%20Statement)
- [Requirements](../../wiki/Requirements)
- [Development Plan](../../wiki/Development%20Plan)
- [Iteration 1 Plan](../../wiki/Iteration%201%20Plan) and [Project Board](../../projects/1)

  ## Demo Users
| Username  | Password        |
|-----------|-----------------|
|   user1   | 123456 |
|   user2   | 123456 |
