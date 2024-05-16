# Generated by Django 5.0.4 on 2024-05-16 06:00

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_remove_customuser_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='runner_category',
            field=models.PositiveIntegerField(choices=[(1, 'Новичок'), (2, 'Любитель'), (3, 'Профи')], db_index=True, default=1, verbose_name='Заявляетесь в группу'),
        ),
        migrations.CreateModel(
            name='Family',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('runner_family', models.ManyToManyField(related_name='runners_family', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]