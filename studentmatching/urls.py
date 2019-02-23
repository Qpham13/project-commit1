from django.conf.urls import url
from django.conf import settings
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import include, path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', auth_views.LoginView.as_view(template_name='studentmatching/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='studentmatching/logout.html'), name='logout'),
    path('admin/', admin.site.urls),
    #url(r'^login/$', auth_views.LoginView.as_view(template_name='studentmatching/login.html'), name='login'),
    #url(r'^logout/$', auth_views.LogoutView.as_view(template_name='studentmatching/logout.html'), name='logout'),
    #url(r'^admin/', admin.site.urls),
    path('', include('social_django.urls', namespace='social')),
]
