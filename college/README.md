# College System Django Project

## Run
1. Extract this ZIP and open a terminal in `college_system_django`.
2. `python -m venv venv`
3. Windows: `venv\\Scripts\\activate` | macOS/Linux: `source venv/bin/activate`
4. `pip install -r requirements.txt`
5. `python manage.py migrate`
6. `python manage.py runserver`
7. Open http://127.0.0.1:8000/

Pages: Home `/`, Students `/students/`, Teachers `/teachers/`.

The two apps use URL namespaces (`students` and `teachers`). Each list page receives a welcome message from its view. Optional add forms redirect to their respective list page. Demo names are stored in memory only and are not permanent.
