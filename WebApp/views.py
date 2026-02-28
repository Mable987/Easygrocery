from itertools import product

from django.shortcuts import render, redirect
from AdminApp.models import *
from WebApp.models import ContactDb, RegistrationDb, CartDb
from django.contrib import messages


# Create your views here.
def Home(request):
    categories = CategoryDb.objects.all()
    latest_products = ProductDb.objects.all().order_by('-id')[:8]
    carts = request.session.get('username')
    cart_count = 0
    if carts:
        cart_count = CartDb.objects.filter(UserName=carts).count()
    return render(request, 'Home.html',{'categories': categories, 'latest_products': latest_products, 'cart_count': cart_count})
def About(request):
    return render(request, 'About.html')
def all_products(request):
    categories = CategoryDb.objects.all()
    products = ProductDb.objects.all()
    latest_products = ProductDb.objects.all().order_by('-id')[:3]
    our_products = ProductDb.objects.all()
    return render(request, 'all_products.html',{'categories': categories, 'products': products, 'latest_products': latest_products, 'our_products': our_products})
def FilteredProducts(request,cat_name):
    products_filtered = ProductDb.objects.filter(Category_Name=cat_name)
    categories = CategoryDb.objects.all()
    return render(request, 'Filtered_Products.html',{'products_filtered': products_filtered, 'categories': categories})
def single_item(request,product_id):
    single_product = ProductDb.objects.get(id=product_id)
    categories = CategoryDb.objects.all()
    return render(request, 'single_item.html',{'single_product': single_product, 'categories': categories})
def contact_page(request):
    categories = CategoryDb.objects.all()
    return render(request, 'Contact_page.html',{'categories': categories})
def save_contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        obj = ContactDb(Name=name, Email=email, Message=message)
        obj.save()
        return redirect(contact_page)
def services(request):
    return render(request, 'services.html')

def sign_in(request):
    return render(request, 'sign_in.html')
def sign_up(request):
    return render(request, 'sign_up.html')
def save_sign_up(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')
        obj = RegistrationDb(UserName=username, Email=email, Password=password, Confirm_Password=confirm_password)
        if RegistrationDb.objects.filter(UserName=username).exists():
            print("User already exists")
            return redirect(sign_up)
        elif RegistrationDb.objects.filter(Email=email).exists():
            print("Email already exists")
            return redirect(sign_up)
        else:
            obj.save()
            messages.success(request, 'Registration successful')
            return redirect(sign_in)
def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        if RegistrationDb.objects.filter(UserName=username,Password=password).exists():
            request.session['username'] = username
            request.session['password'] = password
            return redirect(Home)
        else:
            return redirect(sign_in)
    else:
        return redirect(sign_in)
def user_logout(request):
    del request.session['username']
    del request.session['password']
    return redirect(Home)
def cart(request):
    cart = CartDb.objects.filter(UserName=request.session['username'])
    sub_total = 0
    delivery = 0
    grand_total = 0
    user_data = CartDb.objects.filter(UserName=request.session['username'])
    for i in user_data:
        sub_total += i.TotalPrice
        if sub_total > 1000:
            delivery = 0
        elif sub_total > 500:
            delivery = 40
        else:
            delivery = 70
        grand_total = sub_total + delivery
    return render(request, 'cart.html',{'cart': cart , 'sub_total':sub_total, 'delivery':delivery, 'grand_total':grand_total})
def save_cart(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        productname = request.POST.get('productname')
        quantity = request.POST.get('quantity')
        price = request.POST.get('price')
        totalprice = request.POST.get('total')
        pro = ProductDb.objects.filter(ProductName=productname).first()
        img = pro.ProductImage if pro else None
        obj = CartDb(UserName=username, ProductName=productname,Quantity=quantity,Price=price,TotalPrice=totalprice,ProductImage=img)
        obj.save()
        return redirect(cart)
def delete_cart(request,cart_id):
    cart_delete = CartDb.objects.filter(id=cart_id)
    cart_delete.delete()
    return redirect(cart)

def checkout(request):
    return render(request, 'checkout.html')