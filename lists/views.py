from django.shortcuts import render
from django.http import HttpResponse
from .models import Item

# Create your views here.
def home_page(request):
    if request.method == 'POST':
        item = Item.objects.create(text=request.POST.get('new-item', ''))
        new_item = item.text
    else: 
        new_item = ''

    context = {'new_item': new_item}
    
    return render(request, 'lists/index.html', context)
    
