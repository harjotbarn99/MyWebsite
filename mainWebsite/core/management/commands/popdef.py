from django.core.management.base import BaseCommand
import json
from django.conf import settings
import os
from apps.home.models import *


class Command(BaseCommand):
    help = "Populate the database with my default details."

    def add_arguments(self, parser):
        parser.add_argument(
            "path-to-json",
            type=str,
            nargs="+",
            help="This is the path to json file",
        )

    def handle(self, *args, **kwargs):
        path = kwargs["path-to-json"][0]
        with open(path, "r") as f:
            data = json.loads(f.read())
        for dicti in data:
            if dicti["model"] == "myintro":
                o = MyIntro.objects.create()
                o.greeting_text = dicti["fields"]["greeting_text"]
                o.name = dicti["fields"]["name"]
                o.bio = dicti["fields"]["bio"]
                o.major = dicti["fields"]["major"]
                o.minor = dicti["fields"]["minor"]
                o.micro_credential = dicti["fields"]["micro_credential"]
                o.picture = dicti["fields"]["picture"]
                o.previous_picture = dicti["fields"]["previous_picture"]
                o.email = dicti["fields"]["email"]
                o.resume_link = dicti["fields"]["resume_link"]
                o.save()
            elif dicti["model"] == "project":
                o = Project.objects.create()
                o.title = dicti["fields"]["title"]
                o.name = dicti["fields"]["name"]
                o.category = dicti["fields"]["category"]
                o.description = dicti["fields"]["description"]
                o.in_production = dicti["fields"]["in_production"]
                o.production_link = dicti["fields"]["production_link"]
                o.on_github = dicti["fields"]["on_github"]
                o.github_link = dicti["fields"]["github_link"]
                o.picture = dicti["fields"]["picture"]
                o.previous_picture = dicti["fields"]["previous_picture"]
                o.save()
            elif dicti["model"] == "socialwebsite":
                o = SocialWebsite.objects.create()
                o.site = dicti["fields"]["site"]
                o.link = dicti["fields"]["link"]
                o.classes = dicti["fields"]["classes"]
                o.save()
            else:
                msg = f"{dicti['model']} is an unknown model."
                self.stdout.write(
                    self.style.ERROR(msg)
                )
