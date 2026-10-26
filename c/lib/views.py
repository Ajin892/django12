
from django.shortcuts import render, redirect
from django.db import connection


def create_table():
    with connection.cursor() as cursor:
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS books (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title VARCHAR(100),
                author VARCHAR(100),
                year INTEGER
            )
        """)


def home(request):
    create_table()

    if request.method == "POST":
        title = request.POST.get("title", "").strip()
        author = request.POST.get("author", "").strip()
        year = request.POST.get("year", "").strip()

        if title and author and year:
            try:
                year = int(year)

                with connection.cursor() as cursor:
                    cursor.execute(
                        "INSERT INTO books (title, author, year) VALUES (%s, %s, %s)",
                        [title, author, year]
                    )

                return redirect("home")
            except ValueError:
                pass

    with connection.cursor() as cursor:
        cursor.execute(
            "SELECT id, title, author, year FROM books ORDER BY id DESC"
        )
        books = cursor.fetchall()

    return render(request, "index1.html", {"books": books})


def edit_book(request, book_id):
    create_table()

    with connection.cursor() as cursor:
        cursor.execute(
            "SELECT id, title, author, year FROM books WHERE id = %s",
            [book_id]
        )
        book = cursor.fetchone()

    if book is None:
        return redirect("home")

    if request.method == "POST":
        title = request.POST.get("title", "").strip()
        author = request.POST.get("author", "").strip()
        year = request.POST.get("year", "").strip()

        if title and author and year:
            try:
                year = int(year)

                with connection.cursor() as cursor:
                    cursor.execute(
                        "UPDATE books SET title = %s, author = %s, year = %s WHERE id = %s",
                        [title, author, year, book_id]
                    )

                return redirect("home")
            except ValueError:
                pass

    return render(request, "index1.html", {
        "books": [],
        "book": book,
        "edit_mode": True
    })


def delete_book(request, book_id):
    create_table()

    if request.method == "POST":
        with connection.cursor() as cursor:
            cursor.execute(
                "DELETE FROM books WHERE id = %s",
                [book_id]
            )

    return redirect("home")
