from django import forms
from .models import Book

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ["title", "author", "year"]
        widgets = {
            "title": forms.TextInput(attrs={"placeholder": "Book title"}),
            "author": forms.TextInput(attrs={"placeholder": "Author name"}),
            "year": forms.NumberInput(attrs={"min": 0, "placeholder": "Publication year"}),
        }

    def clean_year(self):
        year = self.cleaned_data["year"]
        if year > 9999:
            raise forms.ValidationError("Enter a valid four-digit year.")
        return year
