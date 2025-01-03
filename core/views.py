from django.shortcuts import render
from django.http import HttpResponse  # Import HttpResponse
from django.db.models import Count

from core.models import Product, Category, Vendor, CartOrder, CartOrderItems, ProductImages, ProductReview, wishlist, Address

def index(request):
    # products = Product.objects.all().order_by("-id")
    products = Product.objects.filter(product_status="published", featured=True).order_by("-id")
    
    context = {
        "products":products
    }
    
    return render(request, 'core/index.html', context)


def product_list_view(request):
    products = Product.objects.filter(product_status="published").order_by("-id")
    
    context = {
        "products":products
    }
    
    return render(request, 'core/product-list.html', context)


def category_list_view(request):
    categories = Category.objects.all()
    
    context = {
        "categories":categories
    }
    
    return render(request, 'core/category-list.html', context)
