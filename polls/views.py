#funcia dlya otpravki text repsonse dlya user
from django.http import HttpResponse #HTTPRESPONSE - object Django
def index(request): #Sozdali funciy otveta. Index - nfsa
    return HttpResponse("Hello, world. You're at the polls index.")  
# Create your views here.
