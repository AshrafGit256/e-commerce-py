from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse  # Import HttpResponse
from django.db.models import Count
from .models import Vendor  # Import the correct model

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

def category_product_list_view(request, cid):
    category = Category.objects.get(cid = cid)
    products = Product.objects.filter(product_status = "published", category = category)
    
    context = {
        "category":category,
        "products":products,
    }
    
    return render(request, "core/category-product-list.html", context)

# def vendor_list_view(request):
#     vendor = vendor.objects.all()
#     context = {
#         "vendor": vendor,
#     }
#     return render(request, "core/vendor-list.html", context)

def vendor_list_view(request):
    vendors = Vendor.objects.all()  # Correct model reference
    context = {
        "vendors": vendors,  # Use a different variable name
    }
    return render(request, "core/vendor-list.html", context)

def vendor_detail_view(request, vid):
    vendor = Vendor.objects.get(vid=vid)  # Correct model reference
    products = Product.objects.filter(vendor=vendor, product_status = "published")
    
    context = {
        "vendor": vendor,  # Use a different variable name
        "products": products,  # Use a different variable name
    }
    return render(request, "core/vendor-detail.html", context)

def product_detail_view(request, pid):
    product =Product.objects.get(pid=pid)
    
    p_image = product.p_images.all()
    
    context = {
        "p": product,  # Use a different variable name
        "p_image": p_image,
    }
    
    return render(request, "core/product-detail.html", context)

# def product_detail_view(request, pid):
#     product = get_object_or_404(Product, pid=pid)
#     p_image = product.p_images.all()
#     return render(request, "core/product-detail.html", {"product": product, "p_image": p_image})