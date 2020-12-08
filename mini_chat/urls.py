"""mini_chat URL Configuration
"""
from chat.api import MessageAPI
from chat.views import index
from chat.views import save as save_message
from core import views
from core.auth_user.api import AuthUserAPI
from django.conf import settings
from django.conf.urls import include, url
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path
from django.views.static import serve
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'api/1/messages', MessageAPI)
router.register(r'api/1/auth_user', AuthUserAPI)

urlpatterns = [
    path('', index, name='index'),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', views.logout, name='logout'),
    path('admin/', admin.site.urls),
    path('signup/', views.signup, name='signup'),
    path('save_messages/', save_message, name='save_messages'),
    url('', include(router.urls)),
    url(r'^accounts/', include('django.contrib.auth.urls')),
    url(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT})
]
