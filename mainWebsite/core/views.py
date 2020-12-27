from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView

# Create your views here.


def default_view(request):
    return HttpResponse("core says hi")

class DefaultView(TemplateView):
    def get_template_names(self):
        return ["core/coming_soon.html"]

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


