# Generated by Django 3.2 on 2021-06-14 18:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('URLshortener', '0008_url_label'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='birth_date',
            field=models.DateField(blank=True, null=True, verbose_name='تاریخ تولد'),
        ),
    ]
