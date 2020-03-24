from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView
from .models import Run
from django.http import HttpResponseRedirect, request
from django.urls import reverse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

class RunListView(ListView):
    model = Run
    template_name = 'runs.html'
    paginate_by = 5

    def get_queryset(self):
        user = self.request.user
        queryset = Run.objects.filter(owner=user).order_by("-date")
        return queryset


class RunCreateView(CreateView):
    model = Run
    fields = ('date', 'description', 'distance', 'time')
    template_name = 'add_run.html'
    success_url = 'runs'

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.owner = self.request.user
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())


class RunDetailView(DetailView):
    model = Run
    template_name = 'run_detail.html'


def delete_run(self, pk):
    run = Run.objects.get(pk=pk).delete()
    return HttpResponseRedirect(reverse('runs'))


class RunUpdateView(UpdateView):
    model = Run
    fields = ('date', 'description', 'distance', 'time')
    template_name = 'edit_run.html'

