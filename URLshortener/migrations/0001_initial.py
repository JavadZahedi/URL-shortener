# Generated by Django 3.2 on 2021-04-28 03:38

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.ImageField(upload_to='profile_images', verbose_name='تصویر')),
                ('birth_date', models.DateField(blank=True, verbose_name='تاریخ تولد')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='URL',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.URLField(max_length=512, verbose_name='آدرس لینک')),
                ('slug', models.SlugField(max_length=8, unique=True, verbose_name='اسلاگ')),
                ('visits', models.PositiveIntegerField(default=0, verbose_name='تعداد بازدید ها')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='تاریخ ایجاد')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='urls', to=settings.AUTH_USER_MODEL, verbose_name='ایجاد کننده')),
            ],
        ),
    ]
