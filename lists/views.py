from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.core.exceptions import ValidationError
from .models import Item, List
from .forms import ItemForm

# Create your views here.
def home_page(request):
    itemform = ItemForm()
    return render(request, 'lists/index.html', {'form': itemform})
    
def new_list(request):
    itemform = ItemForm(data=request.POST)
    if itemform.is_valid():
        list_ = List.objects.create() 
        Item.objects.create(list=list_, text=request.POST['text'])
        return redirect(list_)
    else:
        return render(request, 'lists/index.html', {'form': itemform})
       

def view_list(request, pk):
    list_ = List.objects.get(pk=pk)
    itemform = ItemForm()
    if request.method == "POST":
        itemform = ItemForm(data=request.POST)
        if itemform.is_valid():
            Item.objects.create(text=request.POST['text'], list=list_)
            return redirect(list_)
    context = {'list': list_, 'form': itemform}
    return render(request, 'lists/list.html', context)
    
