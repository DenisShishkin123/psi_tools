from django.views.generic import View, TemplateView, ListView, DetailView, FormView
from django.views.generic import FormView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from .models import  ABCModel
from .forms import ABCModelForm

# #     C
# #     path('create/', views.abc_create, name="abc_create"),
#     path('create/', views.ABCCreate.as_view(), name="abc_create"),
#     # path('list/', views.ABCList.as_view(), name="abc_list"),
#     path('list/', views_crud.ABCList.as_view(), name="abc_list"),
#     path('<int:pk>/', views_crud.ABCDetail.as_view(), name="abc_item"),
# #     CRUDE

# class ABCCreate

class ABCList(ListView):
    # model = ABCModel
    template_name = "abc/abc_list.html"
    context_object_name = "models"
    extra_context = {
        "title": "ABC модели"
    }

    def get_queryset(self):
        return ABCModel.objects.all()

class ABCDetail(DetailView):
    model = ABCModel
    template_name = "abc/abc_item.html"
    context_object_name = "model"
    extra_context = {}
    # pk_url_kwarg = "pk"
    # slug_url_kwarg = "slug"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "ABC модель"
        return context


class AddABC(FormView):
    form_class = ABCModelForm
    template_name = 'abc/abc_create.html'
    # success_url = reverse_lazy('home')
    success_url = reverse_lazy('abc_list')

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)



class CreateABC(CreateView):
    form_class = ABCModelForm
    template_name = 'abc/abc_create.html'
    extra_context={"title": "Добавление"}


class UpdateABC(UpdateView):
    # form_class = ABCModelForm
    model = ABCModel
    fields = "__all__"
    template_name = 'abc/abc_create.html'
    extra_context = {"title": "Изменение"}



















class DeleteABC(DeleteView):
    model = ABCModel
    template_name = 'abc/abc_delete.html'
    success_url = reverse_lazy("abc_list")
    extra_context = {"title": "Удаление"}









