from django.shortcuts import render, HttpResponse
from .models import TodoItem

# Create your views here.
def home(request):
    # render html template or return HTTP response
    return render(request, "home.html")

def todos(request):
    items = TodoItem.objects.all() # get all instances that exist within database field
    # we also pass a dictionary of our todo list items
    # this will be used within the html file
    return render(request, "todos.html", {"todos": items})
