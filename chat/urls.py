from django.conf.urls import url
from django.contrib import admin
# from django.contrib.auth.views import login, logout
from django.contrib.auth import login,logout
from messanger.views import index
from django.contrib.auth.views import LoginView,LogoutView


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$',index,name='homepage'),
    url(r'^accounts/login/$', LoginView.as_view(), name='login'),
    url(r'^accounts/logout/$', LogoutView.as_view(), name='logout'),
    
    # url(r'^accounts/login/$',login, name='login'),  # The base django login view
    # url(r'^accounts/logout/$',logout, name='logout'),  # The base django logout view
]