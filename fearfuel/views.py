from django.shortcuts import render
from account.models import Account 

def fear_fuel_home(request):
    
    context = {
        
    }
    accounts = Account.objects.all()

    return render(request, 'fearfuel/home.html', context)