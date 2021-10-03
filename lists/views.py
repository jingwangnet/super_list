from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Item

# Create your views here.
def home_page(request):
    if request.method == 'POST':
        item = Item.objects.create(text=request.POST.get('new-item', ''))
        return redirect('/')

    return render(request, 'lists/index.html')
    
