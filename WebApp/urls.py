from django.urls import path
from WebApp import views

urlpatterns = [
    path('home/',views.Home,name='home'),
    path('about/',views.About,name='about'),
    path('our_products/',views.all_products,name='our_products'),
    path('filtered_products/<cat_name>/',views.FilteredProducts,name='filtered_products'),
    path('single_item/<int:product_id>/',views.single_item,name='single_item'),
    path('contact_page/',views.contact_page,name='contact_page'),
    path('save_contact/',views.save_contact,name='save_contact'),
    path('services/',views.services,name='services'),
    path('sign_in/',views.sign_in,name='sign_in'),
    path('sign_up/',views.sign_up,name='sign_up'),
    path('save_signup/',views.save_sign_up,name='save_signup'),
    path('user_login/',views.user_login,name='user_login'),
    path('user_logout/',views.user_logout,name='user_logout'),
    path('cart/',views.cart,name='cart'),
    path('save_cart/',views.save_cart,name='save_cart'),
    path('checkout/',views.checkout,name='checkout'),
    path('delete_cart/<int:cart_id>',views.delete_cart,name='delete_cart'),

]