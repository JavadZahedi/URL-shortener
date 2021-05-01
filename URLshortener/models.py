from django.db import models
from django.contrib.auth.models import User
from extensions.time_utils import datetime_to_jalali_str, date_to_jalali_str

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

    @property
    def created_jalali(self):
        return datetime_to_jalali_str(self.created)

    def __str__(self):
        return 'localhost:8000/shortened-url/' + self.slug


class UserProfile(models.Model):
    photo = models.ImageField(upload_to='profile_images', verbose_name='تصویر')
    birth_date = models.DateField(blank=True, verbose_name='تاریخ تولد')
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    @property
    def birth_date_jalali(self):
        return date_to_jalali_str(self.birth_date)

    def __str__(self):
        return ' '.join(self.user.first_name, self.user.last_name)
