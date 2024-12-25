from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import Home,Search,Content,saveArtical,CategoryView,AccountView
urlpatterns = [
    path('',Home,name='home'),
    path('search/',Search,name='search'),
    path('artical/<int:pk>/',Content,name='content'),
    path('artical/saved/',saveArtical,name='SaveArtical'),
    path('<str:category_name>/',CategoryView,name='category_view'),
    path('<str:name1>/<str:name2>/',AccountView,name='accounts')
]

urlpatterns += static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)