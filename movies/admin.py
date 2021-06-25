from django.contrib import admin
from .models import *
# Register your models here.


admin.site.register(Movie)
admin.site.register(Actors)
admin.site.register(MovieActors)
admin.site.register(Directors)
admin.site.register(MovieDirectors)
admin.site.register(Writers)
admin.site.register(MovieWriters)
