from store.models.customer import Customer
from store.forms import Custum
from django.http.response import HttpResponse
from django.shortcuts import render
from .models.product import Product
from django.contrib import messages



# Create your views here.
def index(request):
    prodx = Product.catch_all_products()

    return render(request,'index.html')

def about(request):
    return render(request, 'about.html')


def practice(request):
    prodxx = Product.catch_all_products()
    return render(request, 'practice.html', {'productss':prodxx,})

def register(request):
    if request.method == 'POST':
        f = Custum(request.POST)
        print('POST running...')
        if f.is_valid():
            name = f.cleaned_data['name']
            ph_no = f.cleaned_data['phone_no']
            em = f.cleaned_data['email']
            passs = f.cleaned_data['password']
            


            transfer = Customer(name = name, phoneno = ph_no, email = em, password = passs)
            transfer.save()
            messages.info(request, 'Successfully Registered!!!')
            f = Custum()
    else:
        f = Custum()
        print('GET running...')
    return render(request, 'register.html',{'f':f})



