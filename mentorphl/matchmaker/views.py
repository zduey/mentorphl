from django.shortcuts import render
from django.views.generic import ListView
from django.contrib.auth.mixins import LoginRequiredMixin

from profiles.models import Mentor, Mentee


class MentorList(LoginRequiredMixin, ListView):
    model = Mentor
    template_name = "matchmaker/mentor_list.html"


class MenteeList(LoginRequiredMixin, ListView):
    model = Mentee