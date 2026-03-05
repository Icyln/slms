from django import forms
from .models import Book

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = '__all__'
        widgets = {
            'description': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 3,
            }),
        }