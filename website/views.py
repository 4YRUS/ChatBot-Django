
from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.contrib.auth import authenticate, login, logout
from .chatgpt import send_chat
from .models import record
from django.utils import timezone


global i
i=[0]


def chatbot(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
                message=request.POST.get('message')
                task = record(task=message,created_at=timezone.now())
                task.save()
                response=send_chat(message)
                if message!='':
                    if response:
                        return JsonResponse({'response': response})
                    else:
                        return JsonResponse({'response': 'Your Account Balance is empty Please add Balance and try again...'})

        return render(request,'home.html')
    else:
        return redirect('login')

def user_login(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user = authenticate(request,username=username,password=password)
        if user:
            login(request,user)
            return redirect('home')
        else:
            return redirect('login')
    return render(request,'login.html')

def user_logout(request):
    logout(request)
    return redirect('login')

def history(request):
    if request.user.is_authenticated:
        data=record.objects.all()
        return render(request,'history.html',{'data':data})
    return redirect('login')


