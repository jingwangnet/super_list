from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Item, List

# Create your views here.
def home_page(request):
    return render(request, 'lists/index.html')
    
def new_list(request):
    list_ = List.objects.create()
    item = Item.objects.create(text=request.POST.get('new-item', ''), list=list_)
    return redirect('/list/the-only-url/')

def view_list(request):
    items = Item.objects.all()
    context = {'items': items}
    return render(request, 'lists/list.html', context)
    
