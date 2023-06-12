from django.shortcuts import get_object_or_404, redirect, render
from .models import Product, Cart, Order
from django.contrib.auth import logout

# Create your views here.

def add_to_cart(request, product_id):
    if request.method == 'POST':
        if request.user.is_authenticated:
            user = request.user
            product = get_object_or_404(Product, pk=product_id)
            quantity = request.POST.get('quantity', 1)
            product_type = request.POST.get('product_type')
            details = request.POST.get('details')
            price = request.POST.get('price')
            # Add the product to the cart
            Cart.objects.create(user=user, product=product, quantity=quantity, product_type=product_type, details=details, price = price)
            return redirect('cart')  # Redirect to the cart page
        else:
            # Handle the case when the user is not authenticated
            return redirect('login')
    else:
        # Handle GET request or other methods
        return redirect('index')

def remove_from_cart(request, cart_id):
    if request.user.is_authenticated:
        user = request.user
        cart_item = Cart.objects.get(pk=cart_id, user=user)
        cart_item.delete()
        return redirect('cart')  # Redirect to the cart page
    else:
        # Handle the case when the user is not authenticated
        return redirect('login')

def cart(request):
    if request.user.is_authenticated:
        is_authenticated = request.user.is_authenticated
        username = request.user.first_name
        cart_items = Cart.objects.filter(user=request.user)
        context = {
            'cart_items': cart_items,
            'is_authenticated': is_authenticated,
            'username': username,
        }
        return render(request, 'accounts/cart.html', context)
    else:
        # Handle the case when the user is not authenticated
        return redirect('login')

    
def login(request):
    is_authenticated = request.user.is_authenticated
    if is_authenticated:
        return redirect('/')
    return render(request, 'accounts/login.html')

def google_login(request):

    return render(request, 'accounts/google_login.html')

def logout_view(request):
    logout(request)
    return redirect('/')

def profile(request):
    return redirect('/')

def index(request):
    product_objects = Product.objects.all()

    try:
        username = request.user.first_name
    except:
        username = ''

    is_authenticated = request.user.is_authenticated

    context = {
        'product_objects': product_objects,
        'username': username,
        'is_authenticated': is_authenticated,
    }

    return render(request, 'store/index.html', context)

def product_detail(request, product_id):
    product = get_object_or_404(Product, pk=product_id)


    username = request.user.first_name
    is_authenticated = request.user.is_authenticated

    context = {
        'product': product,
        'is_authenticated': is_authenticated,
        'username': username,
    }
    return render(request, 'store/product_detail.html', context)

def orders(request):
    username = request.user.first_name
    orders = Order.objects.filter(user=request.user)
    is_authenticated = request.user.is_authenticated
    context = {
        'orders': orders,
        'is_authenticated': is_authenticated,
        'username': username,
    }
    if is_authenticated:
        return render(request, 'accounts/orders.html', context)
    return render(request, 'accounts/login.html', context)

def contact(request):
    
    is_authenticated = request.user.is_authenticated
    username = request.user.first_name
    context = {
        'orders': orders,
        'is_authenticated': is_authenticated,
        'username': username,
    }
    return render(request, 'store/contact_us.html', context)