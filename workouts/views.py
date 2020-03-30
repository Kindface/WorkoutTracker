from django.views.generic import ListView, DeleteView
from django.views.generic.edit import CreateView, UpdateView
from .models import Workout
from exercises.models import Exercise
from django.http import HttpResponseRedirect
from django.shortcuts import redirect, get_object_or_404
from .forms import WorkoutCreateForm
from django.shortcuts import render
from django.urls import reverse

class WorkoutListView(ListView):
    model = Workout
    template_name = 'workouts.html'
    paginate_by = 5

    def get_queryset(self):
        user = self.request.user
        queryset = Workout.objects.filter(owner=user).order_by("-id")
        return queryset
'''
def workoutCreate(request):
    form = WorkoutCreateForm(request.user)
    if form.is_valid():
        date = request.POST.get("date")
        print(date)
        form.save()
        return render(request, 'workouts.html', {'form': form})
    else:
        return render(request, 'workout_add.html', {'form': form})




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
'''


class WorkoutCreateView(CreateView):
    success_url = 'workouts'

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

'''
class WorkoutUpdateView(UpdateView):
    def get(self, request, *args, **kwargs):
        context = {'form': WorkoutCreateForm(user=request.user)}
        return render(request, 'edit_workout.html', context)

    def put(self, request, *args, **kwargs):
        form = WorkoutCreateForm(request.POST, user=request.user)
        if form.is_valid():
            workout = form.save(commit=False)
            workout.owner = request.user
            workout.save()
            form.save_m2m()
            return HttpResponseRedirect('workouts')
        return render(request, 'edit_workout.html', {'form': form})
'''

def workout_edit(request, pk):
    #global form
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
        form = WorkoutCreateForm(user=request.user,instance=workout)
    return render(request, 'edit_workout.html', {'form': form})

class WorkoutDetailView(DeleteView):
    model = Workout
    template_name = 'workout_detail.html'


def delete_workout(self, pk):
    workout = Workout.objects.get(pk=pk).delete()
    return HttpResponseRedirect(reverse('workouts'))