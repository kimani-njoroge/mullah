from django.contrib.auth.decorators import login_required
from django.db.models import Sum
from django.shortcuts import render, get_object_or_404

from budget.models import Transaction
from .forms import  TransactionForm


# Create your views here.
@login_required(login_url='/accounts/login/')
def index(request,user_id):
    transactions = Transaction.objects.all()
    print(transactions)
    total = Transaction.objects.aggregate(Sum('price'))['price__sum']
    return render(request,'index.html',{"transactions":transactions,"total":total})

@login_required(login_url='/accounts/login/')
def post(request):
    current_user = request.user
    if request.method == 'POST':
        form = TransactionForm(request.POST,request.FILES)
        if form.is_valid():
            transaction = form.save(commit=False)
            transaction.user = current_user
            transaction.save()
    else:
        form = TransactionForm()
    return render(request,'post.html',{"form":form})
