from django.conf.urls import url

from .views import Mentors, AddMentor, ViewMentor, DeleteMentor, UpdateMentor

app_name = 'mentors'

urlpatterns = [
    url(r'^$', Mentors.as_view(), name='home'),
    url(r'^view/(?P<pk>[0-9]+)/$', ViewMentor.as_view(), name='view'),
    url(r'^add/$', AddMentor.as_view(), name='add'),
    url(r'^update/(?P<pk>[0-9]+)/$', UpdateMentor.as_view(), name='update'),
    url(r'^delete/(?P<pk>[0-9]+)/$', DeleteMentor.as_view(), name='delete'),
]
