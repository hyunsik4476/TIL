# 로그인

## [공식문서](https://docs.djangoproject.com/en/4.0/topics/auth/default/)

## 인증 시스템

### 인증

* 신원 확인
* 사용자가 자신이 누구인지 확인하는 것

### 권한

* 인증된 사용자가 수행할 수 있는 작업을 결정함



## 쿠키와 세션

### HTTP

> Hyper Text Transfer Protocol

* 리소스를 가져오는 것에 대한 통신 프로토콜

### HTTP의 특징

#### 비연결지향

* 서버는 요청에 대한 응답을 보낸 후 연결을 끊음

#### 무상태

* 연결을 끊는 순간 서버 간 통신이 끝나며 상태 정보가 유지되지 않음
* 클라이언트와 서버가 주고 받는 메시지들은 서로 완전히 독립적

### 쿠키

* 서버가 사용자의 웹 브라우저에 전송하는 작은 데이터 조각
* 사용자가 웹을 방문할 경우 해당 웹사이트의 서버를 통해 사용자의 컴퓨터에 설치되는 작은 기록 정보 파일
  * 클라이언트는 쿠키를 로컬에 키 - 밸류 형태로 저장
  * 동일한 서버에 재 요청 시 저장된 쿠키를 함께 전송함

### 쿠키의 역할

* 매 요청마다 쿠키가 함께 넘어가서 클라이언트의 상태(로그인 되어있음 등) 을 함께 전송함
* 우리가 웹사이트와 계속 연결되어 있다고 느껴지는 이유
* HTTP 쿠키는 **상태가 있는** 세션을 만들어 줌

### 쿠키의 사용 목적

* 세션 관리
  * 로그인, 자동 완성, 공지 하루 안보기, 팝업 체크, 장바구니 등
* 개인화
  * 사용자 선호, 테마 등의 설정
* 트래킹
  * 사용자 행동을 기록 및 분석

### 세션

* 클라이언트사 서버에 접속하면 서버가 특정 세션 아이디를 발급하고
* 클라이언트는 발급받은 아이디를 쿠키에 저장
* ID는 세션을 구별하기 위해 필요하며 쿠키에는 ID만 저장함

### 쿠키 수명

* 세션 쿠키 : 종료 시 사라짐
* persistance cookie : 지정 기간동안 유지





## 시작하기

### 두번째 앱 시작하기

* app 이름은 accounts 로 지정하는것을 권장
* 생성 후 settings.py 에 등록



## 로그인 구현하기

### 로그인

[로그인 폼](https://docs.djangoproject.com/en/4.0/topics/auth/default/)

* 로그인은 session을 create 하는 로직과 같음

* django는 이를 위해 인증에 관한 built-in-forms 를 제공

* ```python
  from django.shortcuts import render
  from django.contrib.auth import login as auth_login
  from django.contrib.auth.forms import AuthenticationForm
  
  # Create your views here.
  def login(request):
      if request.method == 'POST':
          form = AuthenticationForm(request, request.POST)
          if form.is_valid():
              auth_login(request, form.get_user())
              return redirect('articles:index')
      else:
          form = AuthenticationForm()
      context = {
          'form': form,
      }
      return render(request, 'accounts/login.html', context)
  ```

* `AuthenticationForm(request, request.POST)` 은 Form 의 상속을 받는 클래스기 때문에 첫 인자로 request 를 받음

* 현재 세션에 연결하려는 인증 된 사용자가 있는 경우 실제 로그인 작업은 login() 함수에서 진행됨

  * request 객체와 user 객체가 필요
  * "인증된" 유저 객체 : form 안에 있을 것 -> `form.get_user()`



## 인증 데이터 출력하기

* ```django
    <div class="container">
      <h3>Hello, {{ user }}</h3>
      <a href="{% url 'accounts:login' %}"></a>
      {% block content %}
      {% endblock content %}
    </div>
  ```

* context 를 넘겨주지 않았는데 왜 `{{ user }}` 가 동작할까?

  * settings.py 의 context_processors 에 템플릿이 렌더링 될 때 자동으로 호출 가능한 컨텍스트 데이터 목록이 존재함



## 로그아웃

* 세션을 삭제하는 것 = session 을 delete 하는 로직과 동일

* logout() 함수가 존재

  * 현재 요청에 대한 세션데이터를 DB와 쿠키에서 삭제됨

* ```python
  from django.contrib.auth import logout as auth_logout
  def logout(request):
      auth_logout(request)
      return redirect('articles:index')
  ```



## 로그인 사용자에 대한 접근 제한

### .is_authenticated 속성값

* 속성값이므로 메소드가 아님에 주의

### login_required 데코레이터

* 사용자가 로그인 되어있지 않으면 settings.LOGIN_URL에 설정된 절대경로로 redirect 함
  * 기본값이 'accounts/login/' 이다



## 문제

* ```python
  @login_required
  @require_POST
  def delete(request, pk):
      article = get_object_or_404(Article, pk=pk)
      if request.method == 'POST':
          article.delete()
          return redirect('articles:index')
      return redirect('articles:detail', article.pk)
  ```

* 이때 첫 데코레이터에 의해 로그인 하게되는 경우, 리다이렉트로 delete로 다시 오게 됨

* redirect 는 get방식의 요청이므로 require_POST에 막히게 된다.

* ```python
  @require_POST
  def delete(request, pk):
      if request.user.is_authenticated:
          article = get_object_or_404(Article, pk=pk)
          article.delete()
      return redirect('articles:index')
  ```

* 데코레이터 중 하나를 내부로 넣어 해결



# 회원가입

## 회원가입

* UserCreationForm 이라는 ModelForm을 사용

* Create 를 user 에 대해 진행한다고 생각하면 편함

* ```python
  def signup(request):
      if request.method == 'POST':
          form = UserCreationForm(request.POST)
          if form.is_valid():
              user = form.save()
              auth_login(request, user)
              return redirect('articles:index')
      else:
          form = UserCreationForm()
      context = {
          'form': form
      }
      return render(request, 'accounts/signup.html', context)
  ```



## 회원탈퇴

* DB에서 user 삭제하기

* ```python
  @require_POST
  def delete(request):
      if request.user.is_authenticated:
          request.user.delete()
          auth_logout(request)
      return redirect('articles:index')
  ```

* DB에서 지우는것과 세션 삭제는 별개이므로 DB에서 지운 뒤 로그아웃 진행



## 회원정보 수정

* UserChangeForm 사용

* 해당 폼의 일부만 사용해야 하므로 forms.py 에서 새 클래스를 만들 예정

### forms.py

* ```python
  from django import forms
  from django.contrib.auth.forms import UserChangeForm
  from django.contrib.auth import get_user_model
  
  class CustomUserChangeForm(UserChangeForm):
  
      class Meta:
          model = get_user_model()
          fields = 
  ```

* `get_user_model` django의 user model 을 받게 해줌



## 비밀번호 변경

* PasswordChangeForm 사용

* ```python
  def change_password(request):
      if request.method == 'POST':
          form = PasswordChangeForm(request.user, request.POST)
          if form.is_valid():
              form.save()
              return redirect('articles:index')
      else:
          form = PasswordChangeForm(request.user)
      context = {
          'form': form,
      }
      return render(request, 'accounts/change_password.html', context)
  ```

* 비밀번호 변경시 세션이 바뀌어 로그아웃됨

* `update_session_auth_hash(request, user)` 함수를 이용해 새로운 password hash 로 session 을 업데이트함

* ```python
  def change_password(request):
      if request.method == 'POST':
          form = PasswordChangeForm(request.user, request.POST)
          if form.is_valid():
              user = form.save()
              update_session_auth_hash(request, user)
              return redirect('articles:index')
      else:
          form = PasswordChangeForm(request.user)
      context = {
          'form': form,
      }
      return render(request, 'accounts/change_password.html', context)
  ```

