from django.shortcuts import HttpResponseRedirect
from django.http import JsonResponse
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import CustomUser
from .send_mail import send_email
# IMPORT ALL DEPENDENCIES OF DJANGO ALLAUTH
# from allauth.socialaccount.signals import pre_social_login
# from allauth.exceptions import ImmediateHttpResponse


@receiver(post_save,sender=CustomUser)
def create_account(sender,instance,created,**kwargs):
    if created:
        send_email(f'email-verified/{instance.id}/{instance.email_token}/',instance.email)

# @receiver(pre_social_login)
# def prevent_social_account_creation(sender,request,sociallogin,**kwargs):
#     if sociallogin.user.email:
#         if CustomUser.objects.filter(email=sociallogin.user.email).exists():
#             return ImmediateHttpResponse(HttpResponseRedirect('/email-verified/message/'))
#         else:
#             return ImmediateHttpResponse(HttpResponseRedirect('/register/'))
#     else:
#         return ImmediateHttpResponse(JsonResponse({"Error":"you can not login with your social account"}))