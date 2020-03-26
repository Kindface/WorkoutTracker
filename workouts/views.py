from django.views.generic import ListView, DeleteView
from django.views.generic.edit import CreateView, UpdateView
from .models import Workout
from exercises.models import Exercise
from django.http import HttpResponseRedirect


class WorkoutListView(ListView):
    model = Workout
    template_name = 'workouts.html'
    paginate_by = 5

    def get_queryset(self):
        user = self.request.user
        queryset = Workout.objects.filter(owner=user).order_by("-id")
        return queryset


class WorkoutCreateView(CreateView):
    model = Workout
    fields = ('date', 'description', 'exercises')
    template_name = 'workout_add.html'
    success_url = 'workouts'

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.owner = self.request.user
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())


class WorkoutDetailView(DeleteView):
    model = Workout
    template_name = 'workout_detail.html'