from django.shortcuts import render
from django.views import generic
from .models import Animal, Exhibit, Zoo

# Create your views here.

def index(request):
	temp = "Hello World!"
	return render(
		request,
		'index.html',
		context = {"temp":temp,},
		)

def map(location):
	temp2 = 1
	return render(
	location,
	"map.html",
	context = {"loc":temp2},
	)

class zoolist(generic.ListView):
	model = Zoo


class zoodetail(generic.DetailView):
	model = Zoo

class exhibit(generic.DetailView):
	model = Exhibit

class animal(generic.DetailView):
	model = Animal

def about(request):
	return render(
	request,
	"about.html",
	context = {}
	)

def contact(request):
	return render(
	request,
	"contact.html",
	context = {}
	)