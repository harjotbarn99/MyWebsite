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
    name = models.CharField(blank=True, max_length=50)
    category = models.CharField(
        max_length=2, choices=TypeOfWork.choices, default=TypeOfWork.PROJECT)
    description = models.TextField(blank=True)
    in_production = models.BooleanField(default=False)
    production_link = models.TextField(blank=True)
    on_github = models.BooleanField(default=False)
    github_link = models.TextField(blank=True)
    picture = models.ImageField(
        default="default_work.png", upload_to="work_thumbnails")
    previous_picture = models.TextField(blank=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if self.name == "":
            self.name = self.title.lower().replace(" ", "_")
        if self.previous_picture and self.previous_picture != self.picture.name and self.previous_picture != "default_work.png" and default_storage.exists(self.previous_picture):
            default_storage.delete(self.previous_picture)
        self.previous_picture = self.picture.name
        return super().save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        previous_picture = self.previous_picture
        ret = super().delete(*args, **kwargs)
        if previous_picture and previous_picture != "default_work.png" and default_storage.exists(previous_picture):
            default_storage.delete(previous_picture)
        return ret


class MyIntro(models.Model):
    greeting_text = models.CharField(max_length=100)
    name = models.CharField(max_length=50)
    bio = models.CharField(max_length=200)
    major = models.CharField(max_length=50, blank=True)
    minor = models.CharField(max_length=50, blank=True)
    micro_credential = models.CharField(max_length=50, blank=True)
    picture = models.ImageField(default='default-me-pic.png')
    #  need to set up S3 to make this
    previous_picture = models.TextField(blank=True)
    email = models.EmailField(max_length=254)
    resume_link = models.TextField(blank=True, default="#")

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if self.previous_picture and self.previous_picture != self.picture.name and self.previous_picture != "default-my-pic.png" and default_storage.exists(self.previous_picture):
            default_storage.delete(self.previous_picture)
        self.previous_picture = self.picture.name
        return super().save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        previous_picture = self.previous_picture
        ret = super().delete(*args, **kwargs)
        if previous_picture and previous_picture != "default-my-pic.png" and default_storage.exists(previous_picture):
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


class HomePage(models.Model):
    default_logo = "def-favicon.ico"
    logo = models.ImageField(default=default_logo)
    previous_logo = models.TextField(blank=True)

    backgrounds_path = "backgrounds"

    intro = models.BooleanField(default=True)
    intro_background_default = "def-intro-back.jpg"
    intro_background = models.ImageField(
        upload_to=backgrounds_path, default=intro_background_default)
    previous_intro_background = models.TextField(blank=True)

    work = models.BooleanField(default=True)
    work_background_default = "def-work-back.jpg"
    work_background = models.ImageField(
        upload_to=backgrounds_path, default=work_background_default)
    previous_work_background = models.TextField(blank=True)

    experience = models.BooleanField(default=True)
    experience_background_default = "def-experience-back.jpg"
    experience_background = models.ImageField(
        upload_to=backgrounds_path, default=experience_background_default)
    previous_experience_background = models.TextField(blank=True)

    about = models.BooleanField(default=True)
    about_background_default = "def-about-back.jpg"
    about_background = models.ImageField(
        upload_to=backgrounds_path, default=about_background_default)
    previous_about_background = models.TextField(blank=True)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        # logo
        self.previous_logo = self.check_and_delete(
            self.logo, self.previous_logo, self.default_logo)
        # intro
        self.previous_intro_background = self.check_and_delete(self.intro_background, self.previous_intro_background,
                                                            self.intro_background_default)
        # work
        self.previous_work_background = self.check_and_delete(self.work_background, self.previous_work_background,
                                                              self.work_background_default)
        # experience
        self.previous_experience_background = self.check_and_delete(self.experience_background, self.previous_experience_background,
                                                                    self.experience_background_default)
        # about
        self.previous_about_background = self.check_and_delete(self.about_background, self.previous_about_background,
                                                               self.about_background_default)

        return super().save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        # logo
        self.delete_pics(
            self.logo, self.default_logo)
        # intro
        self.delete_pics(self.intro_background, self.intro_background_default)
        # work
        self.delete_pics(self.work_background, self.work_background_default)
        # experience
        self.delete_pics(self.experience_background, self.experience_background_default)
        # about
        self.delete_pics(self.about_background, self.about_background_default)
        return super().delete(*args, **kwargs)

    def check_and_delete(self, curr, prev, default):
        if prev and curr.name != prev and prev != default and default_storage.exists(prev):
            default_storage.delete(prev)
        return curr.name

    def delete_pics(self, curr, default):
        if curr.name and curr.name != default and default_storage.exists(curr.name):
            default_storage.delete(curr.name)
        return 

    def __str__(self):
        return "Home page"

    class Meta:
        verbose_name = 'HomePage'
        verbose_name_plural = 'HomePages'


# class Year(models.Model):
#     year = the year 
#     experiences = one to many

#     def __str__(self):
#         pass

#     class Meta:
#         verbose_name = 'Year'
#         verbose_name_plural = 'Years'