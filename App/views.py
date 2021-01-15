from django.shortcuts import render,redirect,HttpResponse
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.core import serializers

from django.core.mail import send_mail
import json
from .models import App,Mails,Forum,Idea,LikeDatas,SaveDatas,CommentDatas
def Login(request):
    # Giriş Olayı Barındırılacak!
    if request.user.is_authenticated:
        return redirect('/home/')
    else:
        if request.method == "POST":
            username = request.POST.get('Username')
            password = request.POST.get('Password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect("/home/")
            else:
                msg = {
                    'msg' : 'false'
                }
                return JsonResponse(msg)
    return render(request,"registration/login.html") 

def createuser(username,email,password):
    user = User.objects.create_user(username=username,email = email,password=password)

def NewAccount(request):
    # Kayıt Olayı Barındırılacak!
    if request.method == "POST":
        username = request.POST.get('Username')
        email = request.POST.get('Email')
        password = request.POST.get('Password')

        createuser(username,email,password)


    return render(request,"NewAccount.html")
@login_required(login_url='/login/')
def home(request):
    return render(request,"home.html")

@login_required(login_url='/login/')
def Logout(request):
    if(request.user.is_authenticated):
        logout(request)
        return redirect('/login/')
    else:
        return redirect('/home/')

@login_required(login_url='/login/')
def Apps(request):
    if request.method == "POST":
        return HttpResponse('Post istek atmamalısın!')
    else:
        #Uygulamalar tablosundaki verileri çek!
        AppsData = App.objects.all().order_by("UpdateDate").reverse()
        context = {
            'data' : AppsData
        }

    return render(request,"apps.html",context)

@login_required(login_url='/login/')
def Ideas(request):
    if request.method == "POST":
        return HttpResponse('Post istek atmamalısın!')
    else:
        # Fikir tablosundaki verileri çek!
        IdeasData = Idea.objects.all().order_by('UpdateDate').reverse()
        context= {
            'data' : IdeasData
        }
    return render(request,"ideas.html",context)

@login_required(login_url='/login/')
def Account(request):
    apps = App.objects.filter(OwnerId = request.user.id).order_by('UpdateDate').reverse()
    ideas = Idea.objects.filter(OwnerId = request.user.id).order_by('UpdateDate').reverse()
    context = {
        'apps' : apps,
        'ideas' : ideas
    }
    return render(request,"account.html",context)


@login_required(login_url='/login/')
def NewApp(request):
    if request.method == "POST":
        header = request.POST.get('header')
        content = request.POST.get('content')
        apptype = request.POST.get('select')
        photo = request.FILES.get('photo')
        link = request.POST.get('link')

        app = App(Owner = request.user.username,OwnerId = request.user.id,AppHeader=header,AppContent=content,AppPhoto = photo,AppType = apptype,AppLink = link)
        app.save()
    return render(request,"NewApp.html")

@login_required(login_url='/login/')
def NewIdea(request):
    if request.method == "POST":
        header = request.POST.get('Header')
        content = request.POST.get('Content')
        apptype = request.POST.get('Type')

        idea = Idea(Owner = request.user.username,OwnerId=request.user.id,IdeaHeader = header,IdeaContent=content,IdeaType=apptype)
        idea.save()
    return render(request,"NewIdea.html")

@login_required(login_url='/login/')
def AppDetail(request,id):
    if request.method == "POST":
        return HttpResponse('Post İstek Atmamalısın!')
    else:
        data = App.objects.get(id = id)
        context = {
            'data' : data
        }
        return render(request,"Appdetail.html",context)

@login_required(login_url='/login/')
def IdeaDetail(request,id):
    if request.method == "POST":
        return HttpResponse('Post İstek Atmamalısın')

    else:
        data = Idea.objects.get(id = id)
        context = {
            'data' : data
        }
        return render(request,"Ideadetail.html",context)


@login_required(login_url='/login/')
def ChangePassword(request):
    if request.method == "POST":
        passwordone = request.POST.get('PasswordOne')
        passwordtwo = request.POST.get('PasswordTwo')
        msg = {}
        if (passwordone == passwordtwo):
            user = User.objects.get(id = request.user.id)
            user.set_password(passwordone)
            user.save()
            msg['msg'] = 'true'
        else:
            msg['msg'] = 'false'
        return JsonResponse(msg)
    return render(request,"ChangePassword.html")

@login_required(login_url='/login/')
def deleteidea(request,id):
    msg = {}
    if request.method == "POST":
        idea = Idea.objects.get(id = id)
        islem = idea.delete()
        if(islem):
            msg['msg'] = 'true'
        else:
            msg['msg'] = 'false'
        return JsonResponse(msg)
    return HttpResponse('Manuel istek atma! :D')

@login_required(login_url='/login/')
def deleteapps(request,id):
    msg = {}
    if request.method == "POST":
        apps = App.objects.get(id = id)
        islem = apps.delete()
        if(islem):
            msg['msg'] = 'true'
        else:
            msg['msg'] = 'false'
        return JsonResponse(msg)
    return HttpResponse('Manuel istek atma! :D') 
@login_required(login_url='/login/')
def sendMail(request):
    msg = {}
    if request.method == "POST":
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        mail = Mails(Owner = request.user.username,OwnerId = request.user.id,OwnerEmail=request.user.email,MailHeader=subject,MailContent=message)
        mail.save()
        if(mail):
            msg['msg'] = 'true'
        else:
            msg['msg'] = 'false'

        return JsonResponse(msg,safe=False)
    return HttpResponse('')       

