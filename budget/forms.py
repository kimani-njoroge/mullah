from  django import forms
from .models import Profile,Transaction


class TransactionForm(forms.ModelForm):
    class Meta:
        model = Transaction
        fields = ['name','price','date']
    date = forms.DateField(widget=forms.DateInput(attrs={'type':'date'}))