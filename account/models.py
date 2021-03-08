from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
# Create your models here.
from urlshortener.models import Url
# from django.db.models.signals import post_save
from django.dispatch import receiver
from .forms import RegisterForm


# class Account(BaseUserManager):
#     def create_user(self, email, name,password=None):
#         my_user = self.model(email=self.normalize_email(email), name=name)
#         my_user.set_password(password)
#         my_user.save()
#         return my_user


# class MyUser(AbstractBaseUser):
#     email = models.EmailField(max_length=60, unique=True)
#     username = models.CharField(max_length=100, blank=True)
#     join_on = models.DateField(auto_now_add=True)

#     object = RegisterForm()
#     USERNAME_FIELD = 'email'
#     REQUIRED_FIELDS = ['username']

# class BlogPost(models.Model):
#     member = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
#     title = models.CharField(max_length=100)

# @receiver(post_save, sender=settings.AUTH_USER_MODEL)
# def update_blog_post(sender, instance, created, **kwargs):
#     if created:
#         BlogPost.objects.create(member=instance) 
#     instance.BlogPost.save()

    
