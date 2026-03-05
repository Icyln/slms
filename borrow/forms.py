from django import forms
from .models import BorrowRecord

class BorrowForm(forms.ModelForm):
    class Meta:
        model = BorrowRecord
        fields = ['borrower_name', 'book', 'borrowed_date', 'return_date', 'is_returned']
        labels = {
            'is_returned': 'Status (Book Returned?)'
        }
        widgets = {
            'borrowed_date': forms.DateInput(attrs={'type': 'date'}),
            'return_date': forms.DateInput(attrs={'type': 'date'}),
            'is_returned': forms.Select(choices=[(False, 'No'), (True, 'Yes')])
        }




