# Generated by Django 4.2.6 on 2023-11-03 05:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cops_app', '0005_rename_cases_police_no_cases_case'),
    ]

    operations = [
        migrations.AddField(
            model_name='case',
            name='is_completed',
            field=models.BooleanField(default=False),
        ),
    ]