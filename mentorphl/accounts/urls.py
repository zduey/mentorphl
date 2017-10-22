from django.conf.urls import url
from django.contrib import admin
from django.contrib.auth import views as auth_views

from .views import *

app_name = 'accounts'

urlpatterns = [
    url(r'^signup/$', UserSignupView.as_view(), name='signup'),
    url(r'^login/$', UserLoginView.as_view(), name='login'),
    url(r'^logout/$', UserLogoutView.as_view(),  name='logout'),
    url(r'^reset/$', UserPasswordResetView.as_view(), name='password_reset'),
    url(r'^reset/done/$', UserPasswordResetDoneView.as_view(), name='password_reset_done'),
    url(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$', 
        UserPasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    url(r'^reset/complete/$', UserPasswordResetCompleteView.as_view(), name='password_reset_complete'),
    url(r'^settings/password/$', UserPasswordChangeView.as_view(), name='password_change'),
    url(r'^settings/password/done/$', UserPasswordChangeDoneView.as_view(), name='password_change_done')
]
