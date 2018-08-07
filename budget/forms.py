from  django import forms
from .models import Profile,Transaction,Category,Ammount

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        exclude = ['user','transaction']