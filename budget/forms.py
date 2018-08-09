from  django import forms
from .models import Profile,Transaction


class TransactionForm(forms.ModelForm):
    class Meta:
        model = Transaction
        exclude = ['user']