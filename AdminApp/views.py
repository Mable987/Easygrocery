from django.core.files.storage import FileSystemStorage
from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.utils.datastructures import MultiValueDictKeyError

from AdminApp.models import CategoryDb


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
    return redirect(view_categories)



def add_products(request):
    return render(request, 'add_products.html')
def view_products(request):
    return render(request, 'view_products.html')
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
