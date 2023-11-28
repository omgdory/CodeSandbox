from django.shortcuts import render, HttpResponse

# Create your views here.
def home(request):
    # render html template or return HTTP response
    return render(request, "home.html")
