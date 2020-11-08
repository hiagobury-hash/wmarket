from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.http import *

def index(request):
        logout(request)
        username = ''
        password = ''

        next_url = request.GET.get('next')

        if request.POST:
            username = request.POST['username']
            password = request.POST['password']

            user = authenticate(username=username, password=password)

            if user is not None:
                if user.is_active:
                    login(request, user)

                    current_user = request.user
                    
                    if next_url:
                        return HttpResponseRedirect(next_url)
                    else:
                        return HttpResponseRedirect('/')
                    
        return render(request, 'login/index.html')