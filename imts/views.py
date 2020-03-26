from django.views.generic import ListView
from django.views.generic.edit import CreateView
from .models import IMT
from django.shortcuts import redirect
from django.http import HttpResponseRedirect
from django.urls import reverse


class IMTListView(ListView):
    model = IMT
    template_name = 'imts.html'
    paginate_by = 5

    def get_queryset(self):
        user = self.request.user
        queryset = IMT.objects.filter(owner=user).order_by("-id")
        return queryset


class ImtCreateView(CreateView):
    model = IMT
    fields = ('height', 'weight')
    template_name = 'add_imt.html'
    success_url = 'imts'

    def post(self, request, *args, **kwargs):
        global result
        weight = request.POST.get("weight")
        height = request.POST.get("height")
        owner = request.user
        test = float(weight)
        test2 = float(height)
        imt = round(abs(test)/(pow(test2, 2)/10000), 1)
        if imt < 16:
            result = "Выраженный дефицит массы тела"
        elif 16 < imt < 18.5:
            result = "Дефицит массы тела"
        elif 18.5 < imt < 25:
            result = "Масса тела в норме"
        elif 25 < imt < 30:
            result = "Избыточная масса тела"
        elif 30 < imt < 35:
            result = "Ожирение первой степени"
        elif 35 < imt < 40:
            result = "Ожирение второй степени"
        elif imt > 40:
            result = "Ожирение третьей степени"
        IMT.objects.create(owner=owner, height=abs(test), weight=abs(test2), imt=imt, result=result)
        return redirect('/imts')


def delete_imt(self, pk):
    imt = IMT.objects.get(pk=pk).delete()
    return HttpResponseRedirect(reverse('imts'))


