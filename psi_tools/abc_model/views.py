from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import View, TemplateView

from .models import ABCModel
from .forms import ABCModelForm

def abc_test(request):
    return render(request, "abc/abc.html")

def abc_list(request):
    models = ABCModel.objects.all()
    context = {
        'title': "ABC модель",
        'models': models,
    }
    return render(request, "abc/abc_list.html", context)

def abc_item(request, id_model):
    model = get_object_or_404(ABCModel, pk=id_model)
    context = {
        'title': "ABC модель",
        'model': model,
    }
    return render(request, "abc/abc_item.html", context)


def abc_create(request):
    if request.method == "POST":
        form = ABCModelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('abc_create')
    else:
        form = ABCModelForm()

    context = {
        'title': 'заполните форму',
        'form': form,
    }

    return render(request, 'abc/abc_create.html', context)

class ABCCreate(View):

    def post(self, request):
        form = ABCModelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('abc_create')
        return render(request, 'abc/abc_create.html', context)

    def get(self, request):
        form = ABCModelForm()

        context = {
            'title': 'заполните форму',
            'form': form,
        }

        return render(request, 'abc/abc_create.html', context)




class ABCList(TemplateView):
    template_name = "abc/abc_list.html"
    extra_context = {
        "title": "ABC модели",
        "models": ABCModel.objects.all(),
    }


