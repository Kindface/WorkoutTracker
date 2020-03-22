from django.shortcuts import render
from django.shortcuts import redirect
from workouts.models import Workout
from django.utils import timezone
from datetime import datetime, timedelta


def check_auth(request):
    if not request.user.is_authenticated:
        return redirect('/login')
    else:
        current_date = timezone.now() - timedelta(days=1)
        print(current_date)
        workout_count = Workout.objects.exclude(date=current_date).filter(owner=request.user).count()
        date = Workout.objects.exclude(date=current_date).filter(owner=request.user).order_by("date").first()
        #print(date)
        if date:
            text = str(date)
            date_workout = datetime.strptime(text, "%Y-%m-%d").date()
            return render(request, 'tracker.html', {'data': date_workout, 'workoutCount': workout_count})
        else:
            workout_error = "Ближайших тренировок не найдено"
            return render(request, 'tracker.html', {'workout_error': workout_error, 'workoutCount': workout_count})
