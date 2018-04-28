from django.shortcuts import render

# Create your views here.

def index(request):
	temp = "Hello World!"
	return render(
		request,
		'index.html',
		context = {"temp":temp,},
		)

def map(location):
	location = 0
	return render(
	"map.html",
	context = {"loc":location},
	)