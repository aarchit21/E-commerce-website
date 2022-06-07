from django.shortcuts import render
from basic_app.models import User
from basic_app.forms import customer_profile,vendor_profile
# Create your views here.
from django.http import HttpResponse,HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.views.generic import CreateView
from django.db import transaction



def index(request):
    return render(request,'basic_app/home.html')

class customer():
    form_class = vendor_profile.UserForm,vendor_profile.UserProfileInfoForm
    def register(request):
        registered=False

        if request.method=='POST':
            cust_user_form=customer_profile.UserForm(request.POST)
            cust_profile_form = customer_profile.UserProfileInfoForm(request.POST)

            if cust_user_form.is_valid() and cust_profile_form.is_valid():
                user = cust_user_form.save(commit=False)
                user.is_cust=True
                user.save()
                user.set_password(user.password)
                user.save()
                profile=cust_profile_form.save(commit=False)
                profile.cust_user = user
                profile.save()
                registered=True
            else:
                print(cust_user_form.errors,cust_profile_form.errors)
        else:
            cust_user_form=customer_profile.UserForm()
            cust_profile_form = customer_profile.UserProfileInfoForm()
        return render(request,'basic_app/custregister.html',{'cust_user_form':cust_user_form,
        'cust_profile_form':cust_profile_form,'registered':registered})

    def user_login(request):
        if request.method=='POST':
            username = request.POST.get('username')
            password = request.POST.get('username')
            user=request.user

            if user.is_authenticated:
                if user.is_active:
                    if user.is_cust:
                        login(request,user)
                        return HttpResponseRedirect(reverse('index'))
                    else:
                        return HttpResponse("This is not a customer account")
                else:
                    return HttpResponse("Account not active")
            else:
                return HttpResponse('<script>alert(\'Invalid login details\');</script>')
        else:
            return render(request,'basic_app/custlogin.html',{})

    @login_required
    def user_logout(request):
        return HttpResponseRedirect(reverse('index'))

class vendor():
    form_class = vendor_profile.UserForm,vendor_profile.UserProfileInfoForm

    def register(request):
        form_class=UserCreationForm
        registered=False

        if request.method=='POST':
            vendor_user_form=vendor_profile.UserForm(request.POST)
            vendor_profile_form = vendor_profile.UserProfileInfoForm(request.POST)

            if vendor_user_form.is_valid() and vendor_profile_form.is_valid():
                user = vendor_user_form.save()
                user.is_vendor=True
                user.save()
                user.set_password(user.password)
                user.save()
                profile=vendor_profile_form.save(commit=False)
                profile.user = user
                profile.save()
                registered=True
            else:
                print(vendor_user_form.errors,vendor_profile_form.errors)
        else:
            vendor_user_form=vendor_profile.UserForm()
            vendor_profile_form = vendor_profile.UserProfileInfoForm()
        return render(request,'basic_app/vendorregister.html',{'vendor_user_form':vendor_user_form,
        'vendor_profile_form':vendor_profile_form,'registered':registered})

    def user_login(request):
        if request.method=='POST':
            username = request.POST.get('username')
            password = request.POST.get('username')
            user=request.user

            if user.is_authenticated:
                if user.is_active:
                    if user.is_vendor:
                        login(request,user)
                        return HttpResponseRedirect(reverse('index'))
                    else:
                        return HttpResponse("This is not a customer account")
                else:
                    return HttpResponse("Account not active")
            else:
                return HttpResponse('<script>alert(\'Invalid login details\');</script>')
        else:
            return render(request,'basic_app/vendorlogin.html',{})

    @login_required
    def user_logout(request):
        return HttpResponseRedirect(reverse('index'))
