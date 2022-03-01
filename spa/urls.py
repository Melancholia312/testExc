from django.urls import path

from .views import BaseView, FilterView

urlpatterns = [
    path('', BaseView.as_view(), name='home'),
    path('filter/', FilterView.as_view(), name='filter_view')
]