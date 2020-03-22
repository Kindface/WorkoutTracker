from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView
from .models import Workout
from django.http import HttpResponseRedirect

class WorkoutListView(ListView):
    model = Workout
    template_name = 'workouts.html'

class WorkoutCreateView(CreateView):
    model = Workout
    fields = ('date', 'description')
    template_name = 'workout_add.html'
    success_url = 'workouts'

    def form_valid(self, form):
        self.object = form.save(commit = False)
        self.object.owner = self.request.user
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())
