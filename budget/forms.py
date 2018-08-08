from  django import forms
from .models import Profile,Transaction,Category

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        exclude = ['user']

class TransactionForm(forms.ModelForm):
    class Meta:
        model = Transaction
        exclude = ['category']