from django.shortcuts import render
from django.http.response import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth import login as login_django

def login(request):
    # tentando fazer longin 
    if request.method=='GET':
        return render(request, 'usuarios/login.html')
        # fazer formulário
    else: 
       username = request.POST.get('email')
       senha =  request.POST.get('senha')
     # modo de usuario verificar se esta correto!

       user = authenticate(username= username, password=senha)

       # autenticação se existe o usuario
       if user:
        login_django(request, user)
        return HttpResponse('Autenticado!')
        
       else:
            return HttpResponse('E-mail ou senha inválidos!')
        
