from django.shortcuts import render
from django.views.generic import TemplateView
from .models import *

# Create your views here.
def base_context(context):
    context["social_websites"] = SocialWebsite.objects.all()
    context["me"] = MyIntro.objects.all().first()
    context["home_page"] = HomePage.objects.all().first()
    return context

class HomeView(TemplateView):
    def get_template_names(self):
        return ["home/home.html"]

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        base_context(context)
        context["works"] = Work.objects.all()
        a = list(Experience.objects.all())
        a.sort(key=lambda ex:ex.start_date)
        a.reverse()
        context["experiences"] = a
        return context