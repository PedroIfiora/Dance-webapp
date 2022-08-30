from django.contrib import messages
from django.shortcuts import render
from .models import Contact

# Create your views here.
def index(request):
    if request.method == "POST":
        name = request.POST.get("name")
        phonenumber = request.POST.get("phonenumber")
        email = request.POST.get("email")
        message = request.POST.get("message")
        contact = Contact(name=name, phone=phonenumber, email=email, message=message)
        contact.save()
        messages.success(request, "Message saved successfully!! Thank you!!!")

    return render(request, 'peterdjangoapp/index.html')
