from django.shortcuts import render


def gallery(request):
    return render(request, "myapp/gallery.html")


def contact(request):
    return render(request, "myapp/contact.html")