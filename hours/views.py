from django.shortcuts import render

def hours(request):
    return render(request, 'hours/hours.html')
