from unicodedata import name
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm

from rest_framework.generics import CreateAPIView

from .forms import OrderDetailsForm

from .models import OrderDetails
from .serializers import *


# Create your views here.
def index(request):
    
    context ={}
 
    # create object of form
    form = OrderDetailsForm(request.POST or None, request.FILES or None)
     
    # check if form data is valid
    if form.is_valid():
        # save the form data to model
        form.save()

    context['form']= form
    return render(request, "home.html", context)


def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('index')
    
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})



class OrderDetailsView(CreateAPIView):
    model = OrderDetails
    serializer_class = OrderDetailsSerializer