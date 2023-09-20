## Installation
1. Cloning the repository
   ```
   git clone https://github.com/mjrchy/ku-polls.git
   ```
2. Access to the project directory
   ```
   cd ku-polls
   ```
3. Create a Virtual Environment and install dependencies
   ```
   python -m venv venv
   . venv\Scripts\activate
   pip install -r requirements.txt
   ```
4. Create .env file and set values for externalized variables following sample.env in the repository
5. Set Up the Database
   ```
   python manage.py migrate
   ```
6. Download data
   ```
   python manage.py loaddata data/users.json
   python manage.py loaddata data/polls.json
   ```
6. Run the server
   ```
   python manage.py runserver
   ```
