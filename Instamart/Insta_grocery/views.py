from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import Product
from .forms import ProductForm
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Home view to display all products and handle product addition
def home(request):
    products = Product.objects.all()
    fm = ProductForm(request.POST or None, request.FILES or None)
    if fm.is_valid():
        fm.save()
        return redirect('home')  # Redirect to home after successful form submission
    return render(request, 'Insta_grocery/home.html', {'products': products, 'fm': fm})

# Edit product view
def edit_product(request, pk):
    product = get_object_or_404(Product, pk=pk)
    fm = ProductForm(request.POST or None, request.FILES or None, instance=product)
    if fm.is_valid():
        fm.save()
        return redirect('home')  # Redirect to home after successful edit
    return render(request, 'Insta_grocery/edit_product.html', {'form': fm, 'product': product})

# Delete product view
def delete_product(request, pk):
    product = get_object_or_404(Product, pk=pk)
    product.delete()
    return redirect('home')  # Redirect to home after successful deletion

@login_required
def Home(request):
    # Replace with your actual product logic
    products = []  # or fetch from DB
    return render(request, 'Register/home.html', {'products': products})
