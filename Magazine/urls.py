from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('user_account.urls')),
    path('',include('home.urls')),
    path('accounts/', include('allauth.urls')),
    path('oauth/',include('social_django.urls'),name='social'),
    path('api-auth/', include('rest_framework.urls'))
]

handler = 'home.views.custom_404_view'