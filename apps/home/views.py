from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.


class HomeView(TemplateView):
    def get_template_names(self):
        return ["home/home.html"]

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context