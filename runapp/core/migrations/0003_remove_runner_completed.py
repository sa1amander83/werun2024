# Generated by Django 5.0.4 on 2024-05-04 17:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_remove_runner_category_updated_runner_nickname'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='runner',
            name='completed',
        ),
    ]
