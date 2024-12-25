from django.shortcuts import render,HttpResponseRedirect
from django.contrib import messages
from django.http import JsonResponse
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.decorators import login_required
from .models import CustomUser,LoginAttempt,PasswordReset
from .Forms import RegisterForm
from .set_cookie import set_cookies
from .send_mail import send_email
# Create your views here.

def Registration(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = CustomUser.objects.create(**form.cleaned_data)           
            is_auth = authenticate(request,username=user.username,password=user.password)
            if is_auth is not None:
                login(request,is_auth)
            response = set_cookies(token=user.cookie_token)
            return response
        else:
            messages.error(request,"Please correct the errors below.")
    form = RegisterForm()
    return render(request,'Account/registeration.html',{'form':form})

def EmailVerifiedMessage(request):
    try:
        user = CustomUser.objects.get(username=request.user.username)
    except CustomUser.DoesNotExist:
        return HttpResponseRedirect('/login/')
    return render(request,'Account/emailVerified.html',{'email':user.email})

@login_required()
def EmailVerfied(request,id,token):
    try:
        user = CustomUser.objects.get(id=id,email_token=token)
    except CustomUser.DoesNotExist:
        return render(request,'Account/some_error.html',{'status_code':404,'title':"We can't find that page",'error':"We're fairly sure that page used to be here, but seems to have gone missing. We do apologize on its behalf."})
    
    user.is_emailVerified = True
    user.save()

    return HttpResponseRedirect('/')

def user_login(request):
    if request.method == 'POST':
        data = request.POST
        username = data.get('username')
        password = data.get('password')
        ip_address = get_client_ip(request)

        if LoginAttempt.check_attempts(ip_address):
            return render(request,'Account/some_error.html',{'status_code':400,'title':'Login Attempt','error':'your account is log please try again after 5 minutes!','url_page':'login'})       
        try:
            user = CustomUser.objects.get(username=username)
        except CustomUser.DoesNotExist:
            # save the login attempts 
            LoginAttempt.objects.create(username=username,ip_address=ip_address)
            return render(request,'Account/login.html',{'error':'Your Username is Incorrect!'})
       
        user_is_auth = authenticate(request,username=user.username,password=password)
        if user_is_auth is not None:
            login(request,user_is_auth)
            send_email(f'email-verified/{user.id}/{user.email_token}/',user.email)
            response = set_cookies(user.cookie_token)
            LoginAttempt.objects.filter(username=username,ip_address=ip_address).delete()
            return response
        else:
            # save the login attempts 
            LoginAttempt.objects.create(username=username,ip_address=ip_address)
            return render(request,'Account/login.html',{'error':'This Password is Incorrect!'})
        
    return render(request,'Account/login.html')

def get_client_ip(request):
    x_forward_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forward_for:
        ip = x_forward_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip

@login_required()
def user_logout(request):
    try:
        user = CustomUser.objects.get(username=request.user.username)
        user.is_emailVerified = False
        user.save()
    except CustomUser.DoesNotExist:
        return render(request,'Account/some_error.html',{'status_code':400,'title':'User DoesNotExist','error':'This User Loged from system Please check and try again.'})
    
    logout(request)

    if 'access_token' in request.COOKIES:
        response = HttpResponseRedirect('/')
        response.delete_cookie('access_token')
        return response
    else:
        return HttpResponseRedirect('/')
    
def PasswordForgot(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        try:
            user = CustomUser.objects.get(email=email)
            PasswordReset.objects.filter(email=email).delete()
        except CustomUser.DoesNotExist:
            return render(request,'Account/passwordMessage.html',{'Response':'if any account with this email exists password reset link will send'})
        client = PasswordReset.objects.create(email=email)
        send_email(f'password-reset/{client.id}/{client.token}/',email,"Please Click on This Link")
        return render(request,'Account/passwordMessage.html',{'Response':'Password Reset Link Sended to Your Email Please Check Your Email'})
    return render(request,'Account/PasswordForgot.html')

def Password_Reset(request,pk,token):
    try:
        userLink = PasswordReset.objects.get(id=pk,token=token)
    except PasswordReset.DoesNotExist:
        return render(request,'Account/some_error.html',{'status_code':404,'title':"We can't find that page",'error':"We're fairly sure that page used to be here, but seems to have gone missing. We do apologize on its behalf."})
    
    user = CustomUser.objects.get(email = userLink.email)

    status = PasswordReset.Check_Links(userLink.email,userLink.token) # check link for expired date
    if status is None:
        userLink.delete()
        return render(request,'Account/some_error.html',{'status_code':404,'title':"We can't find that page",'error':"This Link is expired listen Link after 10 minutes will expired and you can not use that link",})
    
    if request.method == 'POST':
        password = request.POST.get('password')
        confirmPass = request.POST.get('confirm')
        if password == confirmPass:
            user.set_password(password)
            user.save()
            return HttpResponseRedirect('/login/')
        else:
            return render(request,'Account/passwordReset.html',{'error':'Your Password and Confirm Password are not similar'})
    return render(request,'Account/passwordReset.html')