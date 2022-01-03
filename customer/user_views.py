
from django.shortcuts import render, redirect,HttpResponseRedirect, get_object_or_404
from django.http.response import HttpResponse, JsonResponse
from django.db.models import Q
from django.core.paginator import Paginator
from django.conf import settings
from django.contrib.auth import authenticate, login
from .forms import RegistrationForm, LoginForm

from customer.views import index
from .forms import LoginForm, RegistrationForm

def register_user(request):
    register_form = RegistrationForm()
    if request.method == "POST":
        register_form = RegistrationForm(request.POST)
        if register_form.is_valid():
            new_user = register_form.save_user()
            user = authenticate(
                username = new_user.username,
                password= new_user.password,
            )
            login(request,user)
            return redirect('index')

    return render(
        request=request,
        template_name = 'user/register.html',
        context = {
            'register_form' : register_form
        }

    )

def login_user(request):
    login_form = LoginForm()
    if request.method == "POST":
        login_form=LoginForm(request.POST)
        if login_form.is_valid():
            # hàm authenticate nhận username, password người dùng gửi lên
            # lấy trong db auth-user có đúng hay ko?
            user = authenticate(
                username=login_form.cleaned_data['username'],
                password=login_form.cleaned_data['password']
            )
            if user:
                # xác thực thành công
                # giữ trạng thái user đang xác thực
                login(request, user)
                print("Đăng nhập thành công")
                print(request.GET.get('next'))
                if request.GET.get('next'):
                    return HttpResponseRedirect(request.GET.get('next'))
                return redirect('index')
            else:
                print("thông tin không đúng, vui lòng kiểm tra lại")
    return render(
        request=request,
        template_name='user/login.html',
        context={
            'login_form':login_form
        }

    )
    
    