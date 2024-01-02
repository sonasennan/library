from django import forms
from books.models import Book


#form definition
class BookForm(forms.ModelForm):

    class Meta:

        model=Book

        fields="__all__"


