from django.contrib import admin
from .models import *
# Register your models here.


class ActorAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name')
    list_filter = ('last_name', 'first_name')


admin.site.register(Movie)
admin.site.register(Actors, ActorAdmin)
admin.site.register(MovieActors)
admin.site.register(Directors)
admin.site.register(MovieDirectors)
admin.site.register(Writers)
admin.site.register(MovieWriters)
