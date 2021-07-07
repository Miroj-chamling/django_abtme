from os import name
from django.shortcuts import render, HttpResponse
from datetime import datetime
from folio.models import Contact
from django.contrib import messages
# Create your views here.
def index(request):
    return render(request, 'index.html')
    #return HttpResponse('this is homepage')

def about(request):
    return render(request,'about.html')
    # return HttpResponse('this is an about page')
def gallery(request):
    return render(request, 'gallery.html')
    
def contact(request):
    if request.method == "POST":
        firstname = request.POST.get('firstname')
        lastname = request.POST.get('lastname')
        email = request.POST.get('email')
        address = request.POST.get('address')
        city = request.POST.get('city')
        state = request.POST.get('state')
        zip = request.POST.get('zip')
        message = request.POST.get('message')
        date = request.POST.get('firstname')
        contact = Contact(firstname = firstname, lastname = lastname, email = email, address=address, city=city, state=state,
        zip=zip,message=message, date = datetime.today())
        contact.save()
        messages.success(request, 'Your details have been submitted.')
    
    return render(request, 'contact.html')