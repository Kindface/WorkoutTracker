from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView
from .models import Workout
from django.http import HttpResponseRedirect
from django.shortcuts import redirect, get_object_or_404
from .forms import WorkoutCreateForm
from django.shortcuts import render
from django.urls import reverse
from django.contrib.auth.mixins import *


class WorkoutListView(LoginRequiredMixin, ListView):
    model = Workout
    template_name = 'workouts.html'
    paginate_by = 5
    login_url = '/login'

    def get_queryset(self):
        user = self.request.user
        queryset = Workout.objects.filter(owner=user).order_by("-id")
        return queryset


class WorkoutCreateView(LoginRequiredMixin, CreateView):
    success_url = 'workouts'
    login_url = '/login'

    def get(self, request, *args, **kwargs):
        context = {'form': WorkoutCreateForm(user=request.user)}
        return render(request, 'workout_add.html', context)

    def post(self, request, *args, **kwargs):
        form = WorkoutCreateForm(request.POST, user=request.user)
        if form.is_valid():
            workout = form.save(commit=False)
            workout.owner = request.user
            workout.save()
            form.save_m2m()
            return HttpResponseRedirect('workouts')
        return render(request, 'workout_add.html', {'form': form})


def workout_edit(request, pk):
    if not request.user.is_authenticated:
        return redirect('/login')
    else:
        workout = get_object_or_404(Workout, pk=pk)
        if request.method == "POST":
            form = WorkoutCreateForm(request.POST, user=request.user, instance=workout)
            if form.is_valid():
                workout = form.save(commit=False)
                workout.owner = request.user
                workout.save()
                form.save_m2m()
                return redirect('workout_detail', pk=workout.pk)
        else:
            form = WorkoutCreateForm(user=request.user, instance=workout)
        return render(request, 'edit_workout.html', {'form': form})


class WorkoutDetailView(LoginRequiredMixin, DetailView):
    model = Workout
    template_name = 'workout_detail.html'
    login_url = '/login'


def delete_workout(self, pk):
    Workout.objects.get(pk=pk).delete()
    return HttpResponseRedirect(reverse('workouts'))
