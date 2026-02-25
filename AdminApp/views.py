from django.core.files.storage import FileSystemStorage
from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.utils.datastructures import MultiValueDictKeyError

from AdminApp.models import CategoryDb, ProductDb
from WebApp.models import ContactDb
from django.contrib import messages


# Create your views here.
def dashboard(request):
    return render(request, 'dashboard.html')

def add_categories(request):
    return render(request, 'add_categories.html')
def view_categories(request):
    category = CategoryDb.objects.all()
    return render(request, 'view_categories.html', {'categories': category})
def save_category(request):
   if request.method == 'POST':
       categoryname = request.POST.get('categoryname')
       description = request.POST.get('description')
       categoryimage = request.FILES.get('categoryimage')
       obj = CategoryDb(CategoryName=categoryname, Description=description, CategoryImage=categoryimage)
       obj.save()
       messages.success(request, 'Category Added Successfully')
       return redirect(add_categories)
def edit_category(request, category_id):
    data = CategoryDb.objects.get(id=category_id)
    return render(request, 'edit_category.html', {'data': data})
def update_category(request, category_id):
    if request.method == 'POST':
        categoryname = request.POST.get('categoryname')
        description = request.POST.get('description')
        try:
            img = request.FILES.get('categoryimage')
            fs = FileSystemStorage()
            file = fs.save(img.name, img)
        except MultiValueDictKeyError:
            file = CategoryDb.objects.get(id=category_id).CategoryImage
        CategoryDb.objects.filter(id=category_id).update(CategoryName=categoryname, Description=description, CategoryImage=file)
        return redirect(view_categories)
def delete_category(request, category_id):
    category = CategoryDb.objects.filter(id=category_id)
    category.delete()
    messages.error(request, 'Category Deleted Successfully')
    return redirect(view_categories)



def add_products(request):
    categories = CategoryDb.objects.all()
    return render(request, 'add_products.html', {'categories': categories})
def view_products(request):
    products = ProductDb.objects.all()
    return render(request, 'view_products.html',{'products': products})

def save_product(request):
    if request.method == 'POST':
        CategoryName = request.POST.get('categoryname')
        ProductName = request.POST.get('productname')
        Price = request.POST.get('price')
        Description = request.POST.get('description')
        ProductImage = request.FILES.get('productimage')
        obj = ProductDb(Category_Name=CategoryName, ProductName=ProductName, Price=Price, Description=Description,ProductImage=ProductImage)
        obj.save()
        messages.success(request, 'Product Added Successfully')
        return redirect(add_products)
def edit_product(request, product_id):
    product = ProductDb.objects.get(id=product_id)
    categories = CategoryDb.objects.all()
    return render(request, 'edit_products.html', {'product': product, 'categories': categories})
def update_product(request, product_id):
    if request.method == 'POST':
        categoryname = request.POST.get('categoryname')
        ProductName = request.POST.get('productname')
        Price = request.POST.get('price')
        Description = request.POST.get('description')
        try:
            img = request.FILES.get('productimage')
            fs = FileSystemStorage()
            file = fs.save(img.name, img)
        except :
            file = ProductDb.objects.get(id=product_id).ProductImage
        ProductDb.objects.filter(id=product_id).update(Category_Name=categoryname,ProductName=ProductName, Price=Price, Description=Description, ProductImage=file)
        return redirect(view_products)
def delete_product(request, product_id):
    product = ProductDb.objects.get(id=product_id)
    product.delete()
    messages.error(request, 'Product Deleted Successfully')
    return redirect(view_products)







def admin_loginpage(request):
    return render(request, 'admin_login.html')


def admin_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        if User.objects.filter(username__contains=username).exists():
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                request.session['username'] = username
                request.session['password'] = password
                return redirect(dashboard)
            else:
                print("Invalid details..!")
                return redirect(admin_loginpage)
        else:
            print(" User not found..!")
            return redirect(admin_loginpage)
def admin_logout(request):
    del request.session['username']
    del request.session['password']
    return redirect(admin_loginpage)
def contact_data(request):
    contacts = ContactDb.objects.all()
    return render(request, 'contact_data.html',{'contacts': contacts})
