# Library Book Manager (Django)

A simple Django web app to add, view, edit, and delete library books. The homepage displays 5 books per page.

## Setup

1. Install Python 3.10+.
2. Open a terminal in this folder and create a virtual environment (recommended):
   ```bash
   python -m venv venv
   ```
   Activate it:
   - Windows: `venv\Scripts\activate`
   - macOS/Linux: `source venv/bin/activate`
3. Install Django:
   ```bash
   pip install -r requirements.txt
   ```
4. Create the database tables:
   ```bash
   python manage.py makemigrations books
   python manage.py migrate
   ```
5. Start the server:
   ```bash
   python manage.py runserver
   ```
6. Open http://127.0.0.1:8000/

## Features
- Add books (title, author, year)
- List books on the homepage
- Edit and delete books
- Pagination: 5 books per page
- SQLite database by default
