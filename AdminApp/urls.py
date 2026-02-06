from django.urls import path
from AdminApp import views

urlpatterns = [
    path('dashboard/',views.dashboard,name='dashboard'),
    path('add_categories/',views.add_categories,name='add_categories'),
    path('view_categories/',views.view_categories,name='view_categories'),
    path('save_category/', views.save_category, name='save_category'),
    path('edit_category/<int:category_id>',views.edit_category,name='edit_category'),
    path('update_category/<int:category_id>',views.update_category,name='update_category'),
    path('delete_category/<int:category_id>',views.delete_category,name='delete_category'),


    path('add_products/',views.add_products,name='add_products'),
    path('view_products/',views.view_products,name='view_products'),
    path('admin_loginpage/',views.admin_loginpage,name='admin_loginpage'),
    path('admin_login',views.admin_login,name='admin_login'),
    path('admin_logout',views.admin_logout,name='admin_logout'),


]