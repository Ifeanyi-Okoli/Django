from django.shortcuts import render
from django.shortcuts import HttpResponse

# Create your views here.

def index(request): #accept a request object
    return HttpResponse("This works!")

#Django needs to know when it should call the function
#Every view is a stand alone function
#Every view needs to accept a request object
def hello(request): #accept a request object
    return HttpResponse("Congratulations! You have reached the hello page!")