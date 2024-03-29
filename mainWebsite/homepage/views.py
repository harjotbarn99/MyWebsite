from django.shortcuts import render
from django.views.generic import TemplateView
from .models import HomePage, MyIntro, SocialWebsite, Work, Experience, Message

# Create your views here.
def base_context(context):
    context["social_websites"] = SocialWebsite.objects.all()
    context["me"] = MyIntro.objects.all().first()
    context["home_page"] = HomePage.objects.all().first()
    context["messages"] = [Message("This page is not meant to show my UI/UX skills.", "warning")]
    return context

class HomepageView(TemplateView):
    def get_template_names(self):
        # mainWebsite/homepage/templates/homepage/homepage.html
        return ["homepage/homepage.html"]

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        base_context(context)
        context["works"] = Work.objects.all()
        a = list(Experience.objects.all())
        a.sort(key=lambda ex:ex.start_date)
        a.reverse()
        context["experiences"] = a
        return context