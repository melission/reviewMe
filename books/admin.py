from django.contrib import admin
from .models import *
from reviewMe.admin import *
# Register your models here.


class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'published_at')


admin.site.register(Publisher)
admin.site.register(Contributor)
admin.site.register(Book, BookAdmin)
admin.site.register(BookContributor)
admin.site.register(Review)
