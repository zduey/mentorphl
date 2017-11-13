from django.conf.urls import url
from .views import (
    ViewMentorProfile,
    DeleteMentorProfile,
    UpdateMentorProfile
)

app_name = 'profiles'


urlpatterns = [
    url(r'^view/(?P<pk>[0-9]+)/$', ViewMentorProfile.as_view(), name='view'),
    url(r'^update/(?P<pk>[0-9]+)/$', UpdateMentorProfile.as_view(), name='update'),
    url(r'^delete/(?P<pk>[0-9]+)/$', DeleteMentorProfile.as_view(), name='delete'),
]
