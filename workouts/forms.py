from django import forms
from .models import Workout
from exercises.models import Exercise


class WorkoutCreateForm(forms.ModelForm):
    exercises = forms.ModelMultipleChoiceField(queryset=Exercise.objects.none(), widget=forms.CheckboxSelectMultiple)

    class Meta:
        model = Workout
        fields = ('date', 'description', 'exercises')

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super(WorkoutCreateForm, self).__init__(*args, **kwargs)
        self.fields['exercises'].queryset = Exercise.objects.filter(owner=user)


