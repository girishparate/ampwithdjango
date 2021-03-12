from django.shortcuts import render,HttpResponse

# Create your views here.
def home(request,type):
    if(type=='amp'):
        return render(request, 'home.amp.html')
    else:
        return render(request, 'home.html') 