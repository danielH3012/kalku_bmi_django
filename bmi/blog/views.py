# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.


def home(request):
    context = {}
    return render(request,'base/home.html',context)
   
def count(request):
    if request.method == 'POST':
        angka1 = request.POST.get("angka1")
        angka2 = request.POST.get("angka2")
    result = float(angka2)/((float(angka1)/100)**2)
    context = {'result':result}
    return render(request,'base/kalku.html',context)

