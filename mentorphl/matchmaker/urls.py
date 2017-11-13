from django.conf.urls import url
from .views import MentorList


app_name = "matchmaker"


urlpatterns = [
    url(r'^mentors/$', MentorList.as_view(), name='mentors'),
]