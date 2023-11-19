from django.shortcuts import render, HttpResponse

# Create your views here.

def home(request):
    return HttpResponse("home")


def test(request):
    if request.method == "GET":
        return HttpResponse("GET")
    if request.method == "POST":
        return HttpResponse("POST")


def test_slug(request, slug):
    return HttpResponse(f"slug - {slug}")



