from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Product
from .forms import ProductForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import user_passes_test

# Create your views here.


def home(request):
    return HttpResponse("Hello Django!")

def product_list(request):
    products = Product.objects.all()
    return render(request, 'product_list.html', {'products': products})

def is_staff(user):
    return user.is_staff

@login_required
def add_product(request):
    if request.method == "POST":
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save(commit=False)
            if 'image' in request.FILES:
                product.image = request.FILES['image']
            product.save()
            messages.success(request, "Item added successfully!")
            return redirect('product_list')
    else:
        form = ProductForm()
    
    return render(request, 'add_product.html', {'form':form})

@user_passes_test(is_staff)
def edit_product(request, product_id):
    product = Product.objects.get(id=product_id)

    if request.method == "POST" :
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            if 'image' in request.FILES:
                product.image = request.FILES['image']
            product.save()
            messages.success(request, "Items updated successfully!")
            return redirect('product_list')
    else:
        form = ProductForm(instance=product)

    return render(request, 'edit_product.html', { 'form': form, 'product':product})

@user_passes_test(is_staff)
def delete_product(request, product_id):
    product = Product.objects.get(id=product_id)

    if request.method == "POST" :
        product.delete()
        messages.warning(request, "Item deleted successfully!")
        return redirect('product_list')

    return render(request, 'delete_product.html', { 'product':product})

def user_login(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            messages.success(request, f"Welcome back, {user.username}!")
            return redirect('product_list')
    else:
        form = AuthenticationForm()

    return render(request, "login.html", {'form': form})

def user_logout(request):
    logout(request)
    messages.info(request, "You have been logged out succesfully")
    return redirect('login')

def user_signup(request):
    if request.method == "POST" :
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Your account has been created! You can now log in.")
            return redirect('login')
    else:
        form = UserCreationForm()

    return render(request, "signup.html", {'form' : form})




            


