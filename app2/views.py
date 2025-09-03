from django.shortcuts import render

# Create your views here.
def vista1_app2(request):
    return render(request,"app2/v1_app2.html")

def vista2_app2(request):
    return render(request,"app2/v2_app2.html")