# KU Polls

This app helps create surveys with multiple-choice questions specifically for Kasetsart University. It's made by following the [Django Tutorial project](https://docs.djangoproject.com/en/3.1/intro/tutorial01/) and includes extra features. 

A polls application for [Individual Software Process](https://cpske.github.io/ISP) course at [Kasetsart University](https://ku.ac.th).

## How to Run
1. Cloning the repository.
   ```
   git clone https://github.com/mjrchy/ku-polls.git
   ```
2. Access to the project directory.
   ```
   cd ku-polls
   ```
3. Create a Virtual Environment.
   ```
   python -m venv venv
   ```
   On Windows:

   ```
   venv\Scripts\activate
   ```
   On macOS and Linux:
   ```
   source venv/bin/activate
   ```
4. Install dependencies.
   ```
   pip install -r requirements.txt
   ```

5. Create .env file and set values for externalized variables following sample.env in the repository.
6. Set Up the Database.
   ```
   python manage.py migrate
   ```
7. Download data.
   ```
   python manage.py loaddata data/users.json
   python manage.py loaddata data/polls.json
   ```
8. Run the server.
   ```
   python manage.py runserver
   ```

## Project Documents

All project-related documents are in the [Project Wiki](../../wiki/Home)

- [Vision Statement](../../wiki/Vision%20Statement)
- [Requirements](../../wiki/Requirements)
- [Development Plan](../../wiki/Development%20Plan)

## Iteration Plan
- [Iteration 1 Plan](../../wiki/Iteration%201%20Plan) and [Project Board](../../projects/1)
- [Iteration 2 Plan](https://github.com/mjrchy/ku-polls/wiki/Iteration-2-Plan)
- [Iteration 3 Plan](https://github.com/mjrchy/ku-polls/wiki/Iteration-3-Plan) and [Domain Model](https://github.com/mjrchy/ku-polls/wiki/Domain-Model)
- [Iteration 4 Plan](https://github.com/mjrchy/ku-polls/wiki/Iteration-4-Plan)

  ## Demo Users
| Username  | Password        |
|-----------|-----------------|
|   user1   | 123456 |
|   user2   | 123456 |
