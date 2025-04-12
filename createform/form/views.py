from django.shortcuts import render
from .forms import Contactform
# Create your views here.


def Contact(request):
    if request.method == "POST":
        form = Contactform(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']
            return render(request,'index.html', {"name": name})
    else:
        form = Contactform()
    return render(request,'contact.html', {"form": form})
