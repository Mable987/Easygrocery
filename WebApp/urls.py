from django.urls import path
from WebApp import views

urlpatterns = [
    path('home/',views.Home,name='home'),
    path('about/',views.About,name='about'),
    path('our_products/',views.all_products,name='our_products'),
    path('filtered_products/<cat_name>/',views.FilteredProducts,name='filtered_products'),
    path('single_item/<int:product_id>',views.single_item,name='single_item'),
    path('contact_page/',views.contact_page,name='contact_page'),
    path('save_contact/',views.save_contact,name='save_contact'),
    path('services/',views.services,name='services'),
    path('sign_in/',views.sign_in,name='sign_in'),
    path('sign_up/',views.sign_up,name='sign_up'),
    path('save_signup/',views.save_sign_up,name='save_signup'),

]