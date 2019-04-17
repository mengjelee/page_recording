from django.shortcuts import render,redirect   # 加入 redirect 套件
from django.contrib.auth import authenticate
from django.contrib import messages
from django.contrib import auth
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.models import User
from event.models import USER_PATH

def index(request):
    if request.user.is_authenticated: 
        return HttpResponseRedirect('/login/')
    return render(request, 'welnew.html',locals())


def login(request):
    if request.user.is_authenticated:
        #user = auth.authenticate(username=username, password=password)
        user = request.user
        #USER_PATH.objects.create(userName = username,userPath = "Home")  若無此行再次登入時是否會持續記錄?
        #user_p_o = USER_PATH.objects.get(userName=user.username).userPath.all()
        home_path = " Home"
        path_present = USER_PATH.objects.filter(userName=user.username).get()
        p_home_1 = path_present.userPath
        str(p_home_1)
        p_home = p_home_1 + home_path
        print(p_home)
        USER_PATH.objects.filter(userName=user.username).update(userPath = p_home)
        print("go to home")
        path_present = USER_PATH.objects.filter(userName=user.username).get()
        return render(request, 'home.html',locals())

    error = False
    if request.method == 'POST':
        username = request.POST.get('name')
        password = request.POST.get('pass')
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            #if user.is_active:
                auth.login(request,user)
                home_path = " Home"
                path_present = USER_PATH.objects.filter(userName=user.username).get()
                p_home_1 = path_present.userPath
                str(p_home_1)
                p_home = p_home_1 + home_path
                print(p_home)
                USER_PATH.objects.filter(userName=user.username).update(userPath = p_home)
                print("go to home")
                path_present = USER_PATH.objects.filter(userName=user.username).get()
                return render(request, 'home.html', locals())
            #else:
                #return HttpResponse('尚未登入')
        else:
            error = True
            return HttpResponse('登入失敗!')
    #return render(request, 'home.html', locals())

def logout(request):
    auth.logout(request)
    return render(request, 'welnew.html',locals())

def signup(request):
    if request.method == 'POST':
        username = request.POST.get('regname')
        password = request.POST.get('regpass')
        email = ""
        
        # --- 不會顯示登入error! --- #
        try:
            user = User.objects.get(username=username)
        except:
            #user = None
            #if user is None:
            user = User.objects.create_user(username, email, password)
            user.save()
            #messages.add_message(request, messages.INFO, '註冊成功')
            USER_PATH.objects.create(userName = username,userPath = "Home")
            messages.info(request, '註冊成功')
            #print('註冊成功')
        else:
            #messages.add_message(request, messages.INFO, '此使用者已經有人使用')
            messages.info(request, '此使用者已經有人使用')
            #print("此使用者已經有人使用")              
        
        return redirect('/')


def A_page(request):
    user = request.user
    #user_info = USER_PATH.objects.filter(userName=user.username)
    A_path = " A"
    path_present = USER_PATH.objects.filter(userName=user.username).get()
    p_a_1 = path_present.userPath
    str(p_a_1)
    p_a = p_a_1 + A_path
    print(p_a)
    USER_PATH.objects.filter(userName=user.username).update(userPath = p_a)
    print("go to A")
    return render(request, 'A.html',locals())
def B_page(request):
    user = request.user
    #user_info = USER_PATH.objects.filter(userName=user.username)
    B_path = " B"
    path_present = USER_PATH.objects.filter(userName=user.username).get()
    p_b_1 = path_present.userPath
    str(p_b_1)
    p_b = p_b_1 + B_path
    print(p_b)
    USER_PATH.objects.filter(userName=user.username).update(userPath = p_b)
    print("go to B")
    return render(request, 'B.html',locals())
def C_page(request):
    user = request.user
    #user_info = USER_PATH.objects.filter(userName=user.username)
    C_path = " C"
    path_present = USER_PATH.objects.filter(userName=user.username).get()
    p_c_1 = path_present.userPath
    str(p_c_1)
    p_c = p_c_1 + C_path
    print(p_c)
    USER_PATH.objects.filter(userName=user.username).update(userPath = p_c)
    print("go to C")
    return render(request, 'C.html',locals())
def D_page(request):
    user = request.user
    #user_info = USER_PATH.objects.filter(userName=user.username)
    D_path = " D"
    path_present = USER_PATH.objects.filter(userName=user.username).get()
    p_D_1 = path_present.userPath
    str(p_D_1)
    p_D = p_D_1 + D_path
    print(p_D)
    USER_PATH.objects.filter(userName=user.username).update(userPath = p_D)
    print("go to D")
    return render(request, 'D.html',locals())
def E_page(request):
    user = request.user
    #user_info = USER_PATH.objects.filter(userName=user.username)
    E_path = " E"
    path_present = USER_PATH.objects.filter(userName=user.username).get()
    p_E_1 = path_present.userPath
    str(p_E_1)
    p_E = p_E_1 + E_path
    print(p_E)
    USER_PATH.objects.filter(userName=user.username).update(userPath = p_E)
    print("go to E")
    return render(request, 'E.html',locals())
def F_page(request):
    user = request.user
    #user_info = USER_PATH.objects.filter(userName=user.username)
    F_path = " F"
    path_present = USER_PATH.objects.filter(userName=user.username).get()
    p_F_1 = path_present.userPath
    str(p_F_1)
    p_F = p_F_1 + F_path
    print(p_F)
    USER_PATH.objects.filter(userName=user.username).update(userPath = p_F)
    print("go to F")
    return render(request, 'F.html',locals())
def G_page(request):
    user = request.user
    #user_info = USER_PATH.objects.filter(userName=user.username)
    G_path = " G"
    path_present = USER_PATH.objects.filter(userName=user.username).get()
    p_G_1 = path_present.userPath
    str(p_G_1)
    p_G = p_G_1 + G_path
    print(p_G)
    USER_PATH.objects.filter(userName=user.username).update(userPath = p_G)
    print("go to G")
    return render(request, 'G.html',locals())
def H_page(request):
    user = request.user
    #user_info = USER_PATH.objects.filter(userName=user.username)
    H_path = " H"
    path_present = USER_PATH.objects.filter(userName=user.username).get()
    p_H_1 = path_present.userPath
    str(p_H_1)
    p_H = p_H_1 + H_path
    print(p_H)
    USER_PATH.objects.filter(userName=user.username).update(userPath = p_H)
    print("go to H")
    return render(request, 'H.html',locals())
def I_page(request):
    user = request.user
    #user_info = USER_PATH.objects.filter(userName=user.username)
    I_path = " I"
    path_present = USER_PATH.objects.filter(userName=user.username).get()
    p_I_1 = path_present.userPath
    str(p_I_1)
    p_I = p_I_1 + I_path
    print(p_I)
    USER_PATH.objects.filter(userName=user.username).update(userPath = p_I)
    print("go to I")
    return render(request, 'I.html',locals())
def J_page(request):
    user = request.user
    #user_info = USER_PATH.objects.filter(userName=user.username)
    J_path = " J"
    path_present = USER_PATH.objects.filter(userName=user.username).get()
    p_J_1 = path_present.userPath
    str(p_J_1)
    p_J = p_J_1 + J_path
    print(p_J)
    USER_PATH.objects.filter(userName=user.username).update(userPath = p_J)
    print("go to J")
    return render(request, 'J.html',locals())
def result_page(request):
    user = request.user
    #user_info = USER_PATH.objects.filter(userName=user.username)
    result_path = " result"
    path_present = USER_PATH.objects.filter(userName=user.username).get()
    p_result_1 = path_present.userPath
    str(p_result_1)
    p_result = p_result_1 + result_path
    print(p_result)
    USER_PATH.objects.filter(userName=user.username).update(userPath = p_result)
    print("go to result")
    Everyones_data = USER_PATH.objects.all()
    return render(request, 'result.html',locals())
    


