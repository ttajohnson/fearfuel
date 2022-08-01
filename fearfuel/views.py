from multiprocessing import context
from django.shortcuts import render
from account.models import Account 

def fear_fuel_home(request):
    
    context = {
        
    }
    accounts = Account.objects.all()

    return render(request, 'fearfuel/home.html', context)

def consumed_list(request):

    context =  {

    }
    accounts = Account.objects.all()

    return render(request, 'fearfuel/consumed.html', context)

def watchlist(request):

    context = {

    }
    accounts = Account.objects.all()

    return render(request, 'fearfuel/watchlist.html', context)