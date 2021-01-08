from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as gl
from django.core.files.storage import default_storage
# Create your models here.


class Work(models.Model):
    class TypeOfWork(models.TextChoices):
        OPEN_SOURCE = "OS", gl("Open Source")
        PROJECT = "PR", gl("Project")
        CONTRIBUTION = "CB", gl("Contribution")

    title = models.CharField(max_length=50)
    # name is the name giver as slug
    name = models.CharField(max_length=50, blank=True)
    category = models.CharField(
        max_length=2, choices=TypeOfWork.choices, default=TypeOfWork.PROJECT)
    description = models.TextField(blank=True)
    in_production = models.BooleanField(default=False)
    production_link = models.TextField(blank=True)
    on_github = models.BooleanField(default=False)
    github_link = models.TextField(blank=True)
    picture = models.ImageField(
        upload_to="work_thumbnails", default="default_work.png")
    previous_picture = models.TextField(blank=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.name = self.title.lower().replace(" ","_")
        if self.previous_picture != "default_work.png" and default_storage.exists("work_thumbnails/"+self.previous_picture):
            default_storage.delete("work_thumbnails/"+self.previous_picture)
        self.previous_picture = self.picture.name
        return super().save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        previous_picture = self.previous_picture
        ret = super().delete(*args, **kwargs)
        if previous_picture != "default_work.png" and default_storage.exists("work_thumbnails/"+previous_picture):
            default_storage.delete("work_thumbnails/"+previous_picture)
        return ret


class MyIntro(models.Model):
    greeting_text = models.CharField(max_length=100)
    name = models.CharField(max_length=50)
    bio = models.CharField(max_length=200)
    major = models.CharField(max_length=50,blank=True)
    minor = models.CharField(max_length=50,blank=True)
    micro_credential = models.CharField(max_length=50,blank=True)
    picture = models.ImageField(default='default-me-pic.png')
    previous_picture = models.TextField(blank=True)
    email = models.EmailField(max_length=254)
    resume_link = models.TextField(blank=True, default="#")

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if self.previous_picture and self.previous_picture != "my-pic.png" and default_storage.exists(self.previous_picture):
            default_storage.delete(self.previous_picture)
        self.previous_picture = self.picture.name
        return super().save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        previous_picture = self.previous_picture
        ret = super().delete(*args, **kwargs)
        if default_storage.exists(previous_picture):
            default_storage.delete(previous_picture)
        return ret

    class Meta:
        verbose_name = 'My Intro'
        verbose_name_plural = 'My Intros'


class SocialWebsite(models.Model):
    site = models.CharField(max_length=50)
    classes = models.TextField()
    link = models.TextField()

    def __str__(self):
        return self.site

    class Meta:
        verbose_name = 'Social Website'
        verbose_name_plural = 'Social Websites'
