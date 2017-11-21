from django.urls import reverse_lazy
from django.views.generic import ListView, UpdateView, CreateView, DetailView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User

from profiles.models import Mentor


mentor_fields = ['name', 'description', 'thumbnail', 'specialty']


class ViewMentorProfile(LoginRequiredMixin, DetailView):
    model = Mentor
    template_name = 'profiles/mentor_detail.html'
    context_object_name = 'mentor'
    # If mentor does not exist, redirect to add?


class UpdateMentorProfile(LoginRequiredMixin, UpdateView):
    model = Mentor
    fields = mentor_fields
    template_name = 'profiles/update.html'

    def form_valid(self, form):
        """ Set 'complete' member variable of the profile to True """
        form.instance.make_live()
        return super(UpdateMentorProfile, self).form_valid(form)



class DeleteMentorProfile(LoginRequiredMixin, DeleteView):
    model = Mentor
    template_name = 'profiles/delete.html'
    success_url = reverse_lazy('home')

