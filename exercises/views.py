from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView
from .models import Exercise
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.mixins import *


class ExerciseListView(LoginRequiredMixin, ListView):
    model = Exercise
    template_name = 'exercises.html'
    paginate_by = 5
    login_url = '/login'

    def get_queryset(self):
        user = self.request.user
        queryset = Exercise.objects.filter(owner=user)
        return queryset


class ExerciseCreateView(LoginRequiredMixin, CreateView):
    model = Exercise
    fields = ('name', 'sets', 'reps')
    template_name = 'add_exercise.html'
    success_url = 'exercises'
    login_url = '/login'

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.owner = self.request.user
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())


def delete_exercise(self, pk):
    Exercise.objects.get(pk=pk).delete()
    return HttpResponseRedirect(reverse('exercises'))


class ExerciseUpdateView(LoginRequiredMixin, UpdateView):
    model = Exercise
    fields = ('name', 'sets', 'reps')
    template_name = 'edit_exercise.html'
    login_url = '/login'
