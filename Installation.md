## Installation
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
