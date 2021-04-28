from django.db import models
from django.contrib.auth.models import User
import string
import random

# create your managers here


# Create your models here.

class URL(models.Model):
    address = models.URLField(max_length=512, verbose_name='آدرس لینک')
    slug = models.SlugField(max_length=8, unique=True, verbose_name='اسلاگ')
    visits = models.PositiveIntegerField(default=0, verbose_name='تعداد بازدید ها')
    created = models.DateTimeField(auto_now_add=True, verbose_name='تاریخ ایجاد')
    user = models.ForeignKey(User, on_delete=models.CASCADE,
                                  related_name='urls', verbose_name='ایجاد کننده')

    def increase_visits(self):
        self.visits += 1
        self.save()

    def __str__(self):
        return self.slug


class UserProfile(models.Model):
    photo = models.ImageField(upload_to='profile_images', verbose_name='تصویر')
    birth_date = models.DateField(blank=True, verbose_name='تاریخ تولد')
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return ' '.join(self.user.firstname, self.user.lastname)
