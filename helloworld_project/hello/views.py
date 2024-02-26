from django.db import IntegrityError
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.hashers import make_password
import datetime
from .models import Feed

# Create your views here.
def home(request):
    # objects들이 바로 쿼리셋
    blogs = Blog.objects
    return render(request, 'home.html', {'blogs' : blogs})

def new(request):
    return render(request, 'new.html')

def create(request):
    if(request.method == 'POST'):
        post = Blog() # 새 블로그 객체
        post.title = request.POST['title']
        post.body = request.POST['body']
        post.password = request.POST['password']
        post.save()
    return redirect('home')

def register(request):
    if(request.method == 'GET'):
        return render(request, 'register.html')
    
    elif(request.method == 'POST'):
        userid = request.POST.get('userid', None)
        nickname = request.POST.get('nickname', None)
        email = request.POST.get('email', None)
        password =  request.POST.get('password', None)
        password_check =  request.POST.get('password check', None)
        res_data = {}
        try: # 닉네임 중복 검사
            other = BoardMember.objects.get(nickname=nickname)
        except:
            other = None
        if not (userid and nickname and email and password and password_check):
            res_data['error'] = '모든 값을 입력해야합니다'
        elif other is not None:   
            res_data['error'] = '이미 사용 중인 닉네임입니다'
        elif password != password_check:
            res_data['error'] = '비밀번호를 확인해주세요'
        else:
            member = BoardMember()
            member.userid = userid
            member.nickname = nickname
            member.email = email
            member.password = make_password(password)
            try:
                member.save()
            except IntegrityError as e:
                res_data['error'] = '이미 사용 중인 아이디입니다'
        
        if len(res_data) > 0:
            return render(request, 'register.html', res_data)
        return redirect('home')



def helloworld(request):
    return render(request, 'helloworld.html')
def goodbyeworld(request):
    return render(request, 'goodbyeworld.html')


