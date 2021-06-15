from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.conf import settings

from extensions.time_utils import datetime_to_jalali_str, date_to_jalali_str

# create your managers here


# Create your models here.

class URL(models.Model):
    label = models.CharField(blank=True, max_length=30, verbose_name='عنوان')
    address = models.URLField(max_length=512, verbose_name='نشانی اینترنتی')
    slug = models.SlugField(max_length=8, unique=True, verbose_name='اسلاگ')
    visits = models.PositiveIntegerField(default=0, verbose_name='تعداد بازدید ها')
    created = models.DateTimeField(auto_now_add=True, verbose_name='تاریخ ایجاد')
    last_visit = models.DateTimeField(default=timezone.now, verbose_name='آخرین بازدید')
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='urls',
                               verbose_name='ایجاد کننده')

    def increase_visits(self):
        self.visits += 1
        self.last_visit = timezone.now()
        self.save()

    def last_visit_jalali(self):
        return datetime_to_jalali_str(self.last_visit)
    last_visit_jalali.short_description = 'آخرین بازدید'

    def created_jalali(self):
        return datetime_to_jalali_str(self.created)
    created_jalali.short_description = 'تاریخ ایجاد'

    def __str__(self):
        host = settings.ALLOWED_HOSTS[0] if settings.ALLOWED_HOSTS else 'localhost:8000'
        return '{}/shortened-url/{}'.format(host, self.slug)

    class Meta:
        verbose_name = 'نشانی اینترنتی'
        verbose_name_plural = 'نشانی های اینترنتی'


class UserProfile(models.Model):
    photo = models.ImageField(upload_to='profile_images', blank=True, verbose_name='تصویر')
    birth_date = models.DateField(null=True, blank=True, verbose_name='تاریخ تولد')
    website = models.URLField(blank=True, verbose_name='وب سایت')
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')

    def birth_date_jalali(self):
        return date_to_jalali_str(self.birth_date)
    birth_date_jalali.short_description = 'تاریخ تولد'

    def __str__(self):
        return self.user.username

    class Meta:
        verbose_name = 'پروفایل'
        verbose_name_plural = 'پروفایل ها'
