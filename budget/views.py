from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404

from budget.models import Transaction
from .forms import CategoryForm, TransactionForm


# Create your views here.
@login_required(login_url='/accounts/login/')
def index(request):
    return render(request,'index.html')

@login_required(login_url='/accounts/login/')
def post(request):
    current_user = request.user
    if request.method == 'POST':
        form = CategoryForm(request.POST,request.FILES)
        tform = TransactionForm(request.POST,request.FILES)
        if all([form.is_valid(),tform.is_valid]):
            category = form.save(commit=False)
            transaction = form.save(commit=False)
            category.user = current_user
            transaction.user = current_user
            category.save()
            transaction.save()
    else:
        form = CategoryForm()
        tform = TransactionForm()
    return render(request,'post.html',{"form":form,"tform":tform})
