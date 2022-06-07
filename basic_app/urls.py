from django.urls import path
from basic_app import views

app_name = 'basic_app'

urlpatterns = [
    path('customer/register/',views.customer.register,name="cust_register"),
    path('vendor/register',views.vendor.register,name="vendor_register"),
    path('customer/login',views.customer.user_login,name='cust_login'),
    path('vendor/login',views.vendor.user_login,name='vendor_login'),

]
