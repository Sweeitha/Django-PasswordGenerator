from django.shortcuts import render
from django.http import HttpResponse
import random

def welcome(request):
    return render(request, 'pwdgen/homepage.html')
#goes to homepage file in pwdgen template and execute

def admin(request):
    return render(request, 'pwdgen/adminpage.html')

def password(request):
    alpha=list('abcdefghijklmnopqrstuvwxyz')
    length=int(request.GET.get("Length of the password", 12))
#Fetches info from path(request), 12 is the default value
    if request.GET.get("Uppercase"):
        alpha.extend(list('abcdefghijklmnopqrstuvwxyz'.upper()))
    if request.GET.get("Numbers"):
        alpha.extend(list('0123456789'))
    if request.GET.get("Special Character"):
        alpha.extend(list('!@#$%^&*()'))
    passwordtobe=''
    for i in range(length):
        passwordtobe=passwordtobe+random.choice(alpha)
    return render(request, 'pwdgen/passwordpage.html', {'pwd':passwordtobe})
