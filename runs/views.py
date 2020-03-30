from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView
from .models import Run
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.mixins import *


class RunListView(LoginRequiredMixin, ListView):
    model = Run
    template_name = 'runs.html'
    paginate_by = 5
    login_url = '/login'

    def get_queryset(self):
        user = self.request.user
        queryset = Run.objects.filter(owner=user).order_by("-id")
        return queryset


class RunCreateView(LoginRequiredMixin, CreateView):
    model = Run
    fields = ('date', 'description', 'distance', 'time')
    template_name = 'add_run.html'
    success_url = 'runs'
    login_url = '/login'

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.owner = self.request.user
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())


def delete_run(self, pk):
    Run.objects.get(pk=pk).delete()
    return HttpResponseRedirect(reverse('runs'))


class RunUpdateView(LoginRequiredMixin, UpdateView):
    model = Run
    fields = ('date', 'description', 'distance', 'time')
    template_name = 'edit_run.html'
    login_url = '/login'

