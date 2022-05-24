from django.shortcuts import render


# Create your views here.


def home(request):
    return render(request, "home/index.html")


def about(request):
    return render(request, "about/index.html")


def login(request):
    return render(request, "login/index.html")

#return HttpResponse(" <c> Login page </c> ")
