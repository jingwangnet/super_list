from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.core.exceptions import ValidationError
from .models import Item, List

# Create your views here.
def home_page(request):
    return render(request, 'lists/index.html')
    
def new_list(request):
    list_ = List.objects.create()
    item = Item(text=request.POST['new-item'], list=list_)
    try: 
        item.full_clean()
        item.save()
    except ValidationError:
        list_.delete()
        error = "You can't save an empty item"
        return render(request, 'lists/index.html', {'error': error})
    return redirect(list_)

def view_list(request, pk):
    list_ = List.objects.get(pk=pk)
    error = None
    if request.method == "POST":
        try:
            item = Item(text=request.POST['new-item'], list=list_)
            item.full_clean()
            item.save()
            return redirect(list_)
        except ValidationError:
            error = "You can't save an empty item"
  
    context = {'list': list_, 'error': error}
    return render(request, 'lists/list.html', context)
    
