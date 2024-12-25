from django.urls import path
from .views import Registration,user_login,user_logout,PasswordForgot,Password_Reset,EmailVerfied,EmailVerifiedMessage

urlpatterns = [
    path('register/',Registration,name='register'),
    path('login/',user_login,name='login'),
    path('log-out/',user_logout,name='logout'),
    path('password-forgot/',PasswordForgot,name='passwordForgot'),
    path('password-reset/<int:pk>/<str:token>/',Password_Reset,name='passwordReset'),
    path('email-verified/<int:id>/<str:token>/',EmailVerfied,name='EmailVerified'),
    path('email-verified/message/',EmailVerifiedMessage,name='EmailMessage'),
]