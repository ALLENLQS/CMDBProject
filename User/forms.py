#! /usr/bin/env python3
# -*- coding : utf-8 -*-
# Author     : ALLEN
# @Time      : 2018/11/9 0009 下午 4:02
from django import forms
class CMDBUserForm(forms.Form):
    username = forms.CharField(max_length=32,label='用户账号',widget=forms.TextInput(attrs={'class':'form-control'}))
    password = forms.CharField(max_length=32,label='用户密码',widget=forms.PasswordInput(attrs={'class':'form-control'}))
    nickname = forms.CharField(max_length=32,label='用户姓名',widget=forms.TextInput(attrs={'class':'form-control'}))
    phone = forms.CharField(max_length=32,label='用户手机',widget=forms.TextInput(attrs={'class':'form-control'}))
    email = forms.EmailField(label='用户邮箱',widget=forms.EmailInput(attrs={'class':'form-control'}))
    photo = forms.ImageField(label='用户头像')

    def clean_phone(self):
        '''必须写在forms的类里面
	    校验的函数名称必须是clean_字段名称
	    所有要校验的数据都可以同cleaned_data.get(字段)得到
	    如果判断没有符合条件，必须诱发validationError
	    如果判断符合条件,必须将值返回出来
        '''
        data = self.cleaned_data.get('phone')
        if len(data) < 11:
            raise forms.ValidationError('手机号码不可以小于11位')
        else:
            return data


class loginForm(forms.Form):
    username = forms.CharField(
        max_length=32,
        label='用户账号',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control'
            }
        )
    )
    password = forms.CharField(
        max_length=32,
        label='用户密码',
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control'
            }
        )
    )