from unittest import runner

from django.contrib import admin

# Register your models here.
from core.models import Runner, Teams


class TeamsAdmin(admin.ModelAdmin):
    search_fields = ('team',)
    list_display = ('team',)
    list_display_links = ('team',)

    list_filter = ('team',)
    ordering = ('team',)
    list_per_page = 50
    list_max_show_all = 100


class RunnerAdmin(admin.ModelAdmin):
    # resource_class = TeamsAdmin
    # def пробег_за_день(self, username, day_distance=None):
    #     result = RunnerDay.objects.filter(user__user__username=username).filter(
    #         user__runnerday__day_distance=day_distance)
    #
    #     return result
    #
    # def дистанция_за_день(self, username):
    #     result = RunnerDay.objects.filter(user__user__username=username)
    #     return result
    #
    # def время_пробега(self, username):
    #     result = RunnerDay.objects.filter(user__user__username=username)
    #     return result
    #
    # def средний_темп(self, username):
    #     result = RunnerDay.objects.filter(user__user__username=username)
    #     return result

    # fields = ('пробег_за_день', 'дистанция_за_день', 'время_пробега', 'средний_темп',)
    search_fields = (
        'runner', 'runner_team__team', 'runner_age', 'runner_category', 'runner_gender', 'zabeg22')
    list_editable = ('runner_age', 'runner_category', 'runner_gender', 'zabeg22', 'zabeg23')
    list_display = ('runner', 'runner_team', 'runner_age', 'runner_category', 'runner_gender', 'zabeg22', 'zabeg23')
    # 'пробег_за_день','дистанция_за_день', 'время_пробега', 'средний_темп',)
    # list_display = ('user', 'runner_age', 'runner_category', 'runner_gender', 'zabeg22', )
    list_display_links = ('runner', 'runner_team',)

    # list_filter = ('runner_category','category_updated','completed', 'is_admin', 'runner_team',)
    ordering = ('runner',)

    list_per_page = 50
    list_max_show_all = 50


admin.site.register(Teams, TeamsAdmin)
admin.site.register(Runner, RunnerAdmin)
