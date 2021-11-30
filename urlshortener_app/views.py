from django.shortcuts import render, redirect
from django.http import HttpResponse
import uuid  
from .models import Urlshortener 
# Create your views here.
def index(request):
    return render(request, 'index.html')

def create_view(request):
    if request.method == 'POST':
        url = request.POST['link']
        uid = str(uuid.uuid4())[:7]
        new_url = Urlshortener(link=url, uuid=uid)
        new_url.save()
        return HttpResponse(uid)


def go_view(request, pk):
    url_info = Urlshortener.objects.get(uuid=pk)
    return redirect(url_info.link)