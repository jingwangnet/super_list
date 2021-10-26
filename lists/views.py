from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.core.exceptions import ValidationError
from .models import Item, List
from .forms import ItemForm, ExistingListItemForm

# Create your views here.
def home_page(request):
    itemform = ItemForm()
    return render(request, 'lists/index.html', {'form': itemform})
    
def new_list(request):
    itemform = ItemForm(data=request.POST)
    if itemform.is_valid():
        list_ = List.objects.create() 
        itemform.save(for_list=list_)
        return redirect(list_)
    else:
        return render(request, 'lists/index.html', {'form': itemform})
       

def view_list(request, pk):
    list_ = List.objects.get(pk=pk)
    itemform = ExistingListItemForm(for_list=list_)
    if request.method == "POST":
        itemform = ExistingListItemForm(data=request.POST, for_list=list_ )
        if itemform.is_valid():
            itemform.save()
            return redirect(list_)
    context = {'list': list_, 'form': itemform}
    return render(request, 'lists/list.html', context)
    
