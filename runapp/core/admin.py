from unittest import runner

from django.contrib import admin

# Register your models here.
from core.models import Runner

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
        'user__username', 'runner_team__team', 'runner_age', 'runner_category', 'runner_gender', 'zabeg22')
    list_editable = ('runner_age', 'runner_category', 'runner_gender', 'zabeg22','zabeg23')
    list_display = ('user', 'runner_team', 'runner_age', 'runner_category', 'runner_gender', 'zabeg22', 'zabeg23')
    # 'пробег_за_день','дистанция_за_день', 'время_пробега', 'средний_темп',)
    # list_display = ('user', 'runner_age', 'runner_category', 'runner_gender', 'zabeg22', )
    list_display_links = ('user', 'runner_team',)

    # list_filter = ('runner_category','category_updated','completed', 'is_admin', 'runner_team',)
    ordering = ('user__username',)

    list_per_page = 50
    list_max_show_all = 50

admin.site.register(Runner, RunnerAdmin)