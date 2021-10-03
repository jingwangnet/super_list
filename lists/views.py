from django.shortcuts import render
from django.http import HttpResponse
from .models import Item

# Create your views here.
def home_page(request):
    item = Item(text=request.POST.get('new-item', ''))
    item.save()

    context = {'new_item': item.text}
    
    return render(request, 'lists/index.html', context)
    
