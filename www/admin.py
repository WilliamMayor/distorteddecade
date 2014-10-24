from django.contrib import admin

# Register your models here.
from django.contrib import admin
from www.models import Gig, Intro


class GigAdmin(admin.ModelAdmin):
    fields = ['where', 'when', 'description', 'more']
    list_display = ('where', 'when')


class IntroAdmin(admin.ModelAdmin):
    fields = ['name', 'intro']
    list_display = ('name',)


admin.site.register(Gig, GigAdmin)
admin.site.register(Intro, IntroAdmin)
