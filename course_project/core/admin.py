from django.contrib import admin
from .models import HomePage, About, BelowBanner, AboutPoint, ClientFeedback


@admin.register(HomePage)
class HomePageAdmin(admin.ModelAdmin):
    list_display = ['title', 'description']


admin.site.register(BelowBanner)
admin.site.register(ClientFeedback)


class PointInlineAdmin(admin.StackedInline):
    model = AboutPoint
    extra = 1


@admin.register(About)
class AboutAdmin(admin.ModelAdmin):
    list_display = ['title']
    inlines = [PointInlineAdmin]
