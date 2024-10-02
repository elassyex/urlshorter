from django.shortcuts import render, redirect
from django.http import HttpResponse
import uuid
from .models import Make

global mao
def home(request):

    return render(request, 'base/index.html')
mao = {"link":"",
      "uuid":""}
def create(request):
    global mao
    if request.method == 'POST':
        link = request.POST['link']
        if 'https://' not in link:
            link = 'https://' + link
            
        uid = str(uuid.uuid4())[:5]
        mao ={"link":link,
             "uuid":uid}
        # newmake = Make(link=link, uuid=uid)
        # newmake.save()
        return HttpResponse(uid)

def go(request, pk):
    global mao
    for key, val in mao.items():
        if key == 'uuid' and val == str(pk):
            urla=mao.get('link')
    #urla = mao.get(uuid=pk)
    return redirect(urla)
