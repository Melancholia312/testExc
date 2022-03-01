from django.shortcuts import render
from django import views
from django.forms.models import model_to_dict

from .models import SomeObj
from .forms import FilterForm
from .services import my_filter


class BaseView(views.generic.ListView):

    model = SomeObj
    template_name = 'spa/index.html'
    paginate_by = 2
    context_object_name = 'objects'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter_form'] = FilterForm()
        return context


class FilterView(views.generic.ListView):

    model = SomeObj
    template_name = 'spa/index.html'
    paginate_by = 2
    context_object_name = 'objects'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter_form'] = FilterForm(self.request.GET)
        return context

    def get_queryset(self):
        filter_form = FilterForm(self.request.GET)
        queryset = []
        if filter_form.is_valid():
            cleaned_data = filter_form.cleaned_data
            queryset = my_filter(cleaned_data['condition'], cleaned_data['field'], cleaned_data['user_input'])
        return queryset

