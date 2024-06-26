# Generated by Django 5.0.4 on 2024-05-15 13:11

import django.contrib.auth.validators
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Teams',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('team', models.PositiveIntegerField(choices=[(100, 100), (101, 101), (102, 102), (103, 103), (104, 104), (105, 105), (106, 106), (107, 107), (108, 108), (109, 109), (110, 110), (111, 111), (112, 112), (113, 113), (114, 114), (115, 115), (116, 116), (117, 117), (118, 118), (119, 119), (120, 120), (121, 121), (122, 122), (123, 123), (124, 124), (125, 125), (126, 126), (127, 127), (128, 128), (129, 129), (130, 130), (131, 131), (132, 132), (133, 133), (134, 134), (135, 135), (136, 136), (137, 137), (138, 138), (139, 139), (140, 140), (141, 141), (142, 142), (143, 143), (144, 144), (145, 145), (146, 146), (147, 147), (148, 148), (149, 149), (150, 150), (151, 151), (152, 152), (153, 153), (154, 154), (155, 155), (156, 156), (157, 157), (158, 158), (159, 159), (160, 160), (161, 161), (162, 162), (163, 163), (164, 164), (165, 165), (166, 166), (167, 167), (168, 168), (169, 169), (170, 170), (171, 171), (172, 172), (173, 173), (174, 174), (175, 175), (176, 176), (177, 177), (178, 178), (179, 179), (180, 180), (181, 181), (182, 182), (183, 183), (184, 184), (185, 185), (186, 186), (187, 187), (188, 188), (189, 189), (190, 190), (191, 191), (192, 192), (193, 193), (194, 194), (195, 195), (196, 196), (197, 197), (198, 198), (199, 199), (200, 200), (201, 201), (202, 202), (203, 203), (204, 204), (205, 205), (206, 206), (207, 207), (208, 208), (209, 209), (210, 210), (211, 211), (212, 212), (213, 213), (214, 214), (215, 215), (216, 216), (217, 217), (218, 218), (219, 219), (220, 220), (221, 221), (222, 222), (223, 223), (224, 224), (225, 225), (226, 226), (227, 227), (228, 228), (229, 229), (230, 230), (231, 231), (232, 232), (233, 233), (234, 234), (235, 235)], default=100, unique=True, verbose_name='команда')),
            ],
            options={
                'verbose_name': 'команда',
                'verbose_name_plural': 'команды',
            },
        ),
        migrations.CreateModel(
            name='CustomUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('runner_team', models.PositiveIntegerField(db_index=True, verbose_name='команда')),
                ('runner_age', models.PositiveIntegerField(db_index=True, verbose_name='возраст')),
                ('runner_category', models.PositiveIntegerField(choices=[(1, 'Новичок - 50 км'), (2, 'Легкий - 100 км'), (3, 'Средний - 200 км'), (4, 'Тяжелый - 400 км'), (5, 'Ультра - 900 км')], db_index=True, default=1, verbose_name='Заявляетесь в группу')),
                ('runner_gender', models.CharField(choices=[('м', 'м'), ('ж', 'ж')], default='м', max_length=1, verbose_name='пол участника')),
                ('zabeg22', models.BooleanField(default=False, verbose_name='Участник МыZaБег 2022')),
                ('zabeg23', models.BooleanField(default=False, verbose_name='Участник МыZaБег 2023')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'участник',
                'verbose_name_plural': 'участники',
            },
        ),
    ]
