from django.shortcuts import render, redirect
from django.contrib.auth import (
    login as auth_login,
    logout as auth_logout,
    update_session_auth_hash,
)
from django.contrib.auth.models import User
from django.contrib.auth.forms import (
    AuthenticationForm,
    PasswordChangeForm,
)
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST

from .forms import CustomUserChangeForm, CustomUserCreationForm


# Create your views here.
def signup(request):
    """
    - GET: 회원가입 폼이 담긴 페이지 응답
    - POST: 사용자 회원정보 받아서 회원가입 
    """
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('articles:index')
    else:
        form = CustomUserCreationForm()
    context = {
        'form': form,
    }
    return render(request, 'accounts/signup.html', context)


def login(request):
    """
    - GET: 로그인 폼이 담긴 페이지 응답
    - POST: 사용자 로그인 받아서 인증 (authentication) 
    """
    # 로그인 된 사용자 접근 거부
    if request.user.is_authenticated:
        return redirect('posts:index')
    
    if request.method == 'POST':
        # 인증 => 사용자 요청 정보 필수 (아이디, 비밀번호, 세션, 쿠키 ...)
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            user = form.get_user()    
            auth_login(request, user) # 세션 생성 

            # 만약에 쿼리스트링에 next 인자가 있으면
            # 그곳으로 보내고, 그렇지 않으면 메인으로 리다이렉트
            # ex) http://127.0.0.1:8000/accounts/login/?next=/2/edit/
            next_url = request.GET.get('next') # ex) /2/edit/
            
            return redirect(next_url or 'articles:index')
    else:
        form = AuthenticationForm()

    context = {
        'form': form,
    }
    return render(request, 'accounts/login.html', context)


@login_required
@require_POST
def logout(request):
    """
    사용자의 세션을 만료(삭제)시킵니다.
    """
    auth_logout(request)
    return redirect('articles:index')


def update(request):
    """
    - GET: 회원 정보 수정이 가능한 폼 응답
    - POST: 수정된 회원 정보 DB 반영
    """
    if request.method == 'POST':
        form = CustomUserChangeForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('articles:index')
    else:
        form = CustomUserChangeForm(instance=request.user) # 현재 로그인된 유저 객체
    context = {
        'form': form,
    }
    return render(request, 'accounts/update.html', context)
        

@login_required 
def change_password(request):
    if request.method == 'POST':
        # 1) 현재 로그인된 사용자 정보 바인딩 (request.user)
        # 2) 사용자가 보낸 수정된 비밀번호 정보 (request.POST)
        form = PasswordChangeForm(request.user, request.POST) # (작성 순서 중요!!!)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            return redirect('articles:index')
    else:
        form = PasswordChangeForm(user=request.user)
    context = {
        'form': form,
    }
    return render(request, 'accounts/change_password.html', context)