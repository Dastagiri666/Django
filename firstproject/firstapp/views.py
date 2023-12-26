from django.shortcuts import render
from.models import employee

# Create your views here.
def vamsi(request):
    if request.method=="POST":
        a = request.POST["name"]
        b = request.POST["domain"]
        c = request.POST["company"]
        d = employee(name=a,domain=b,company=c)
        d.save()
    x = employee.objects.all()
    return render(request,"hello.html",{"data":x})