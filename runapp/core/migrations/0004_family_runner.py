# Generated by Django 5.0.4 on 2024-05-16 06:54

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_alter_customuser_runner_category_family'),
    ]

    operations = [
        migrations.AddField(
            model_name='family',
            name='runner',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL, verbose_name='Участник'),
            preserve_default=False,
        ),
    ]
