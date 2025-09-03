from django.shortcuts import render

# Create your views here.
def vista1_app1(request):
    return render(request,"app1/v1_app1.html")

def vista2_app1(request):
    return render(request,"app1/v2_app1.html")