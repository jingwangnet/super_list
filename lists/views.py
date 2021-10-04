from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Item, List

# Create your views here.
def home_page(request):
    return render(request, 'lists/index.html')
    
def new_list(request):
    list_ = List.objects.create()
    item = Item.objects.create(text=request.POST.get('new-item', ''), list=list_)
    return redirect(f'/list/{list_.pk}/')

def view_list(request, pk):
    list_ = List.objects.get(pk=pk)
    context = {'list': list_}
    return render(request, 'lists/list.html', context)
    
def add_item(request, pk):
    list_ = List.objects.get(pk=pk)
    item = Item.objects.create(text=request.POST.get('new-item', ''), list=list_)
    return redirect(f'/list/{list_.pk}/')
