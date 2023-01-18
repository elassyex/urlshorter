from django.shortcuts import render, redirect
from django.http import HttpResponse
import uuid
from .models import Make

def home(request):

    return render(request, 'base/index.html')

def create(request):
    if request.method == 'POST':
        link = request.POST['link']
        uid = str(uuid.uuid4())[:5]
        newmake = Make(link=link, uuid=uid)
        newmake.save()
        return HttpResponse(uid)

def go(request, pk):
    urla = Make.objects.get(uuid=pk)
    return redirect(urla.link)