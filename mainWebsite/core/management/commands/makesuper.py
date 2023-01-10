from django.contrib.auth import get_user_model
from django.core.management.base import BaseCommand
from django.conf import settings

class Command(BaseCommand):
    def handle(self, *args, **options):
        User = get_user_model()
        username_ = settings.CONFIG_YAML["App"]["superuser_username"]
        password_= settings.CONFIG_YAML["App"]["superuser_password"]
        email_= settings.CONFIG_YAML["App"]["superuser_email"]
        if not User.objects.filter(username=username_).exists():
            #  change the username, email and password before use
            #   it is recomended to use environment variables for this to avoid pushing sensitive 
            #      info in remote repository
            
            User.objects.create_superuser(username_, email_, password_)
            s = "'"+username_ +"' user has created with password '"+password_+"' and email "+email_
            self.stdout.write(self.style.SUCCESS(s))
        else:
            self.stdout.write(self.style.SUCCESS("admin user already exists"))

