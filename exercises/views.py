from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView
from .models import Exercise
from django.http import HttpResponseRedirect


class ExerciseListView(ListView):
    model = Exercise
    template_name = 'exercises.html'
    paginate_by = 5

    def get_queryset(self):
        user = self.request.user
        queryset = Exercise.objects.filter(owner=user)
        return queryset


class ExerciseCreateView(CreateView):
    model = Exercise
    fields = ('name', 'sets', 'reps')
    template_name = 'add_exercise.html'
    success_url = 'exercises'

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.owner = self.request.user
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())

