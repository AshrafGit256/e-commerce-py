from core.models import Category, Address

def default(request):
    categories = Category.objects.all()
    
    # Handle cases where the user may not have an address
    address = None
    if request.user.is_authenticated:
        address = Address.objects.filter(user=request.user).first()  # Using .first() avoids errors

    return {
        'categories': categories,
        'address': address,
    }
