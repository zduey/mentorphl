from django.urls import reverse_lazy
from django.views.generic import ListView, UpdateView, CreateView, DetailView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User

from mentors.models import Mentor


mentor_fields = ['name', 'description', 'thumbnail']


class Mentors(LoginRequiredMixin, ListView):
    model = Mentor
    template_name = "mentors/mentor_list.html"


class ViewMentor(LoginRequiredMixin, DetailView):
    model = Mentor
    template_name = 'mentors/mentor_detail.html'
    context_object_name = 'mentors'

class AddMentor(LoginRequiredMixin, CreateView):
    model = Mentor
    template_name = 'mentors/add.html'
    fields = mentor_fields
    success_url = reverse_lazy('mentors:home')

    def form_valid(self, form):
        """ Auto-populate the recipe owner field """
        form.instance.owner = self.request.user
        return super(AddMentor, self).form_valid(form)

class UpdateMentor(LoginRequiredMixin, UpdateView):
    model = Mentor
    fields = mentor_fields
    template_name = 'mentors/add.html'
    success_url = reverse_lazy('mentors:home')

class DeleteMentor(LoginRequiredMixin, DeleteView):
    model = Mentor
    template_name = 'mentors/delete.html'
    success_url = reverse_lazy('mentors:home')

