from django.shortcuts import redirect,HttpResponseRedirect
import uuid

def refresh_token():
    token = uuid.uuid4
    return token

def set_cookies(token):
    response = HttpResponseRedirect('/email-verified/message/')
    response.set_cookie(
        key='access_token',
        value=token,
        max_age=2592000,
        httponly=True,
        secure=True,
        samesite='Lax'
    )
    return response