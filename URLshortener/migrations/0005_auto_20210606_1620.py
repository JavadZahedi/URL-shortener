# Generated by Django 3.2 on 2021-06-06 11:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('URLshortener', '0004_auto_20210530_1814'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='website',
            field=models.URLField(blank=True, verbose_name='وب سایت'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='photo',
            field=models.ImageField(blank=True, upload_to='profile_images', verbose_name='تصویر'),
        ),
    ]