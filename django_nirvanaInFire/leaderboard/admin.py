from django.contrib import admin
from leaderboard.models import Leaderboard,HeroInfo
# Register your models here.
# class HeroInline(admin.TabularInline):
#     model = HeroInfo
#     extra = 3
class LeaderboardAdmin(admin.ModelAdmin):
    list_display = ['boardtitle','bpub_time']
    # inlines = [HeroInline]
class HeroInfoAdmin(admin.ModelAdmin):
    list_display = ['hname','gender','hcontent','hbtitle']
    list_filter = ['hname']
    search_fields = ['hname','hcontent']
    list_per_page = 3
admin.site.register(Leaderboard,LeaderboardAdmin)
admin.site.register(HeroInfo,HeroInfoAdmin)
