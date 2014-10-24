from django.contrib import admin

# Register your models here.
from django.contrib import admin
from www.models import Gig


class GigAdmin(admin.ModelAdmin):
    fields = ['where', 'when', 'description', 'more']
    list_display = ('where', 'when')


admin.site.register(Gig, GigAdmin)
