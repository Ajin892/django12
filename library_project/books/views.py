from django.shortcuts import get_object_or_404, redirect, render
from django.core.paginator import Paginator
from .forms import BookForm
from .models import Book

def book_list(request):
    paginator = Paginator(Book.objects.all(), 5)
    page_obj = paginator.get_page(request.GET.get("page"))
    return render(request, "books/book_list.html", {"page_obj": page_obj})

def book_create(request):
    if request.method == "POST":
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("book_list")
    else:
        form = BookForm()
    return render(request, "books/book_form.html", {"form": form, "heading": "Add a book"})

def book_update(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == "POST":
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect("book_list")
    else:
        form = BookForm(instance=book)
    return render(request, "books/book_form.html", {"form": form, "heading": "Edit book"})

def book_delete(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == "POST":
        book.delete()
        return redirect("book_list")
    return render(request, "books/book_confirm_delete.html", {"book": book})
