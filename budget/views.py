from django.contrib.auth.decorators import login_required
from django.db.models import Sum
from django.shortcuts import render, get_object_or_404, redirect

from budget.models import Transaction
from .forms import  TransactionForm
import csv
from django.http import HttpResponse
from .resources import TransactionResource


# Create your views here.
@login_required(login_url='/accounts/login/')
def index(request):
    user = request.user
    transactions = Transaction.objects.filter(user=user)
    print(transactions)
    tots = Transaction.objects.filter(user=user)
    total = tots.aggregate(Sum('price'))['price__sum']
    print(total)
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
            return redirect(index)
    else:
        form = TransactionForm()
    return render(request,'post.html',{"form":form})

def export(request):
    user = request.user
    transaction_resource = TransactionResource()
    queryset = Transaction.objects.filter(user=user)
    dataset = transaction_resource.export(queryset)
    response = HttpResponse(dataset.csv,content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="Transactions.csv"'
    return response

def xls(request):
    user = request.user
    transaction_resource = TransactionResource()
    queryset = Transaction.objects.filter(user=user)
    dataset = transaction_resource.export(queryset)
    response = HttpResponse(dataset.xls,content_type='application/vnd.ms-excel')
    response['Content-Disposition'] = 'attachment; filename="Transactions.xls"'
    return response
