# Generated by Django 3.2 on 2021-06-06 12:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('URLshortener', '0005_auto_20210606_1620'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='birth_date',
            field=models.DateField(blank=True, null=True, verbose_name='تاریخ تولد'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to='profile_images', verbose_name='تصویر'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='website',
            field=models.URLField(blank=True, null=True, verbose_name='وب سایت'),
        ),
    ]
