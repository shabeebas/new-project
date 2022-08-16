from django.shortcuts import render

# Create your views here.
def loginpage(request):
    return render(request,"loginpage.html")
def newpage(request):
    return render(request,"newpage.html") 
def masterpage(request):
    return render(request,"masterpage.html")       