from django.shortcuts import render
from .models import Place,People

# Create your views here.
def demo(request):
    Places=Place.objects.all()
    namess=People.objects.all()
    return render(request,'index.html',{'result':Places,'results':namess})