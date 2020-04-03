from django.shortcuts import render
from django.shortcuts import redirect
from workouts.models import Workout
from runs.models import Run
from django.utils import timezone
from django.db.models import Sum


def check_auth(request):
    if not request.user.is_authenticated:
        return redirect('/login')
    else:
        current_date = timezone.now()
        workout_count = Workout.objects.filter(date__gte=current_date, owner=request.user).count()
        distance_sum = Run.objects.filter(owner=request.user).aggregate(Sum('distance'))['distance__sum']
        nearest_date_workout = Workout.objects.filter(date__gte=current_date, owner=request.user).order_by("date").first()
        nearest_date_run = Run.objects.filter(date__gte=current_date, owner=request.user).order_by("date").first()
        return render(request, 'tracker.html', {'date_workout': nearest_date_workout, 'workoutCount': workout_count, 'distance_sum': distance_sum, 'date_run': nearest_date_run})
