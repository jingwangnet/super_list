from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home_page(request):
    context = {'new_item': request.POST.get('new-item', '')}
    return render(request, 'lists/index.html', context)
    
