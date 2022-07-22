from django.shortcuts import render

def fear_fuel_home(request):
    print(request.headers)
    return render(request, 'fearfuel/home.html', {})