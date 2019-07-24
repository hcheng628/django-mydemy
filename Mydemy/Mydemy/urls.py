"""Mydemy URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.views.static import serve
import xadmin

from Mydemy.settings import MEDIA_ROOT
from users.views import LoginView, RegisterView, ActivateView, ForgetPwdView, ResetPwdView,\
    DoResetPwdView, LogOutView, HomeView


urlpatterns = [
    url(r'^xadmin/', xadmin.site.urls),
    url(r'^captcha/', include('captcha.urls')),
    url('^$', HomeView.as_view(), name='home'),
    url(r'^login/$', LoginView.as_view(), name='login'),
    url(r'^logout/$', LogOutView.as_view(), name='logout'),
    url(r'^register/$', RegisterView.as_view(), name='register'),
    url(r'^active/(?P<verification_code>.*)/$', ActivateView.as_view(), name='active'),
    url(r'^forgetpwd/$', ForgetPwdView.as_view(), name='forget_pwd'),
    url(r'^resetpwd/(?P<verification_code>.*)/$', ResetPwdView.as_view(), name="reset_pwd"),
    url(r'^do_resetpwd/$', DoResetPwdView.as_view(), name='do_reset_pwd'),
    url(r'^org/', include('organizations.urls', namespace='org')),
    url(r'^course/', include('courses.urls', namespace='course')),
    url(r'^user/', include('users.urls', namespace='user')),
    url(r'^media/(?P<path>.*)/$', serve, {'document_root': MEDIA_ROOT}),
    #url(r'^static/(?P<path>.*)/$', serve, {'document_root': STATIC_ROOT}),
    url(r'^ueditor/',include('DjangoUeditor.urls')),
]

handler404 = 'users.views.handler404'
handler500 = 'users.views.handler500'
