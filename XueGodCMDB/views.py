#! /usr/bin/env python3
# -*- coding : utf-8 -*-
# Author     : ALLEN
# @Time      : 2018/11/13 0013 下午 2:24
from django.shortcuts import render,render_to_response,HttpResponse,HttpResponseRedirect
from User.forms import CMDBUserForm
from Server.models import CMDBUser
from XueGodCMDB.settings import BASE_DIR
from django.http import JsonResponse
import os
# Create your views here.
# def base(request):
#     return render_to_response('blank.html')

def loginValid(func):
    def valid(request,*args,**keywords):
        username = request.COOKIES.get('username')
        if username:
            try:
                user = CMDBUser.objects.get(username=username)
            except:
                return HttpResponseRedirect('/login/',locals())
            else:
                return func(request)
        else:
            return HttpResponseRedirect('/login/',locals())
    return valid

@loginValid
def index(request):
    register_forms = CMDBUserForm()
    if request.method == 'POST' and request.POST and request.FILES:
        register_data = CMDBUserForm(data=request.POST,files=request.FILES)
        if register_data.is_valid():
            register_post_data = register_data.cleaned_data

            username = register_post_data.get('username')
            password = register_post_data.get('password')
            nickname = register_post_data.get('nickname')
            phone = register_post_data.get('phone')
            email = register_post_data.get('email')
            # 当去get图片的时候，get到的是个对象,用.name的方法获取photo的值
            photo = register_post_data.get('photo').name

            CMDBUser.objects.create(
                username = username,
                password = password,
                nickname = nickname,
                phone = phone,
                email = email,
                photo = photo,
            )
            photofile = request.FILES.get('photo')
            photoSavePath = os.path.join(BASE_DIR,'static\\images\\%s'%photofile.name)
            with open(photoSavePath,'wb') as pf:
                for chunk in photofile.chunks():
                    pf.write(chunk)
        else:
            print(register_data.errors)
    return render(request, 'index.html', locals())


def login(request):
    result_dict = {'submit': 'success'}
    if request.method =='POST' and request.POST:
        # 获取普通cookie
        login_cookie = request.COOKIES.get('login_cookie')
        if login_cookie:
            data = request.POST
            username = data.get('username')
            password = data.get('password')
            try:
                user = CMDBUser.objects.get(username = username)
            except:
                result_dict['submit'] = 'name error'
                return JsonResponse(result_dict)
            else:
                db_password = user.password
                if password == db_password:
                    response = HttpResponseRedirect('/index/',locals())
                    response.set_cookie(key='username',value=user.username)
                    return response
                else:
                    result_dict['submit'] = 'pwd error'
                    return JsonResponse(result_dict)
        else:
            return HttpResponse('404')
    else:
        # 生成response实例
        response =  render(request,'login.html')
        # 普通cookie
        response.set_cookie("login_cookie","helloworld",max_age=3600)
        # # 加盐cookie
        # response.set_signed_cookie("login_cookie","hello world",salt="likeyougirl",max_age=3600)
        return response

def logout(request):
    valid = request.COOKIES.get("login_cookie")
    response = HttpResponseRedirect("/login/")
    if valid == "helloworld":
        response.delete_cookie(valid)
    return response

# user_db = {
#     "username":"allen",
#     "password":"123"
# }
# def login_v1(request):
#     result = {"status":"","data":""}
#     if request.method == 'POST' and request.POST:
#         login_data = request.POST
#         user = login_data.get('username')
#         pwd = login_data.get('password')
#         if user == user_db['username']:
#             if pwd == user_db['password']:
#                 response = HttpResponseRedirect("/")
#                 response.set_cookie(key="valid",value="login_v1")
#                 return response
#             else:
#                 result["status"] = "error"
#                 result["data"] = "密码错误"
#         else:
#             result["status"] = "error"
#             result["data"] = "用户名不存在"
#     return render(request,'login_v1.html',result)
#
# def loginValid_v1(func):
#     def valid(request,*args,**kwargs):
#         valid = request.COOKIES.get("valid")
#         if valid == "login_v1":
#             return func(request)
#         else:
#             return HttpResponseRedirect("/login_v1/")
#     return valid
# @loginValid_v1
# def index_v1(request):
#     valid = request.COOKIES.get("valid")
#     if valid == "login_v1":
#         return render(request,"index_v1.html")
#     else:
#         return HttpResponseRedirect("/login_v1/")