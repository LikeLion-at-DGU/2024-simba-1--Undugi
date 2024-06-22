from django.shortcuts import render, redirect
from django.contrib import auth, messages
from django.contrib.auth.models import User
from django.contrib.auth.hashers import check_password
from .models import Profile

# Create your views here.
# 로그인/로그아웃
def login(request):
    if request.method == 'POST':
        id = request.POST['id']
        password = request.POST['password']

        user = auth.authenticate(request, username=id, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('main:mainpage') # alert(?)
        else:
            messages.warning(request, '가입 정보가 없는 아이디예요.')
            return render(request, 'accounts/login.html')
        
    elif request.method == 'GET':
        return render(request, 'accounts/login.html')
    
def logout(request):
    auth.logout(request)
    return redirect('main:mainpage')

# 회원가입
def signup1(request):
    if request.method == 'POST':
        if request.POST['password'] == request.POST['confirm']:
            request.session['id'] = request.POST['id']
            request.session['password'] = request.POST['password']
            # 중복 아이디 방지
            try:
                user_profile = User.objects.get(username = request.POST['id'])
                messages.warning(request, '이미 존재하는 아이디입니다. 다른 아이디로 시도해 보세요.')
                return render(request, 'accounts/signup.html')
            except User.DoesNotExist:
                user_profile = None     # 출력 어떻게 할지 의논
            return redirect('accounts:signup2')
    return render(request, 'accounts/signup.html')

def signup2(request):
    if request.method == 'POST':
        request.session['nickName'] = request.POST['nickName']
        # 닉네임 중복 방지
        try:
            user_profile = Profile.objects.get(nickName = request.POST['nickName'])
            messages.warning(request, '이미 존재하는 닉네임입니다. 다른 닉네임을 입력해 주세요.')
            return render(request, 'accounts/signup2.html')
        except Profile.DoesNotExist:
            user_profile = None

        request.session['major'] = request.POST['major']
        request.session['weight'] = request.POST['weight']
        request.session['gender'] = request.POST['gender']
        request.session['agegroup'] = request.POST['agegroup']
        return redirect('accounts:signup3')
    return render(request, 'accounts/signup2.html')

def signup3(request):
    if request.method == 'POST':
        user = User.objects.create_user(
            username=request.session['id'],
            password=request.session['password']
        )
        user.profile.nickName = request.session['nickName']
        user.profile.major = request.session['major']
        user.profile.weight = request.session['weight']
        user.profile.gender = int(request.session['gender'])
        user.profile.agegroup = request.session['agegroup']

        user.profile.goal = request.POST['goal']

        user.profile.save()

        auth.login(request, user)
        return redirect('/')
    return render(request, 'accounts/signup3.html')

# 아이디/비밀번호 찾기
def idpasswordfind(request):
    return render(request, 'accounts/idpasswordfind.html')

# 아이디 찾기
def idfindv1(request):
    if request.method == 'POST':
        nickname = request.POST.get('nickName', '')
        password = request.POST.get('password', '')
        major = request.POST.get('major', '')

        try:
            user_profile = Profile.objects.get(nickName=nickname, major=major)
            user = user_profile.user
            if check_password(password, user.password):
                return render(request, 'accounts/idfindv2.html', {'username': user.username})
            else:
                messages.warning(request, "비밀번호가 일치하지 않습니다.")
                return render(request, 'accounts/idfindv1.html', {'error':'비밀번호가 일치하지 않습니다.'})
        except Profile.DoesNotExist:
            messages.warning(request, "일치하는 사용자를 찾을 수 없습니다.")
            return render(request, 'accounts/idfindv1.html', {'error':'일치하는 사용자를 찾을 수 없습니다.'})
    return render(request, 'accounts/idfindv1.html')

def idfindv2(request):
    return render(request, 'accounts/idfindv2.html')

# 비밀번호 재설정
def passwordfindv1(request):
    if request.method == 'POST':
        nickname = request.POST.get('nickName', '')
        id = request.POST.get('id', '')
        major = request.POST.get('major', '')

        try:
            user_profile = Profile.objects.get(nickName=nickname, major=major)
            user = user_profile.user
            if user.username == id:
                request.session['user_id'] = user.id
                return render(request, 'accounts/passwordfindv2.html')  # 비밀번호 재설정 페이지
            else:
                messages.warning(request, '아이디가 일치하지 않습니다.')
                return render(request, 'accounts/passwordfindv1.html', {'error':'아이디가 일치하지 않습니다.'})
        except Profile.DoesNotExist:
            messages.warning(request, "일치하는 사용자를 찾을 수 없습니다.")
            return render(request,'accounts/passwordfindv1.html', {'error':'일치하는 사용자를 찾을 수 없습니다.'})
    return render(request, 'accounts/passwordfindv1.html')

def passwordfindv2(request):
    if request.method == 'POST':
        password = request.POST.get('password', '')
        confirm = request.POST.get('confirm', '')

        if password == confirm:
            user_id = request.session.get('user_id')
            if user_id:
                try:
                    user = User.objects.get(id=user_id)
                    user.set_password(password)
                    user.save()
                    messages.warning(request, '비밀번호 변경이 완료되었습니다.')
                    return render(request, 'accounts/passwordfindv1.html')   #passwordfindv3.html 생기면 경로 변경
                except User.DoesNotExist:
                    messages.warning(request, '일치하는 사용자를 찾을 수 없습니다.')
                    return render(request, 'accounts/passwordfindv1.html')
        else:
            messages.warning(request, '비밀번호가 일치하지 않습니다.')
    return render(request, 'accounts/passwordfindv2.html')