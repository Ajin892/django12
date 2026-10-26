DJANGO VISIT COUNTER WEBSITE

Requirements:
- Python 3.10+
- Internet connection for the first install (to install Django)

HOW TO RUN (Windows / VS Code terminal):
1. Extract this ZIP file.
2. Open a terminal in the extracted homework5 folder.
3. Install Django:
   python -m pip install -r requirements.txt
4. Create the database tables:
   python manage.py migrate
5. Start the server:
   python manage.py runserver
6. Open http://127.0.0.1:8000/ in your browser.

Features:
- Sign up with username and password
- Log in and log out
- Visit Counter page requires login
- Counts visits separately for each logged-in user's session
- SQLite database is used for Django authentication

Note:
The visit count is stored in the session. It remains available for that browser session
and may reset when the session expires or is cleared.
