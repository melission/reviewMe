from django.contrib import admin
from .models import *
from reviewMe.admin import *
# Register your models here.


class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'isnb_with_dashes', 'published_at')

    def isnb_with_dashes(self, obj):
        """ '9780316769174' => '978-0-31-676917-4' """
        return '{}-{}-{}-{}-{}'.format(
            obj.isbn[0:3], obj.isbn[3:4], obj.isbn[4:6], obj.isbn[6:12], obj.isbn[12:13])




admin.site.register(Publisher)
admin.site.register(Contributor)
admin.site.register(Book, BookAdmin)
admin.site.register(BookContributor)
admin.site.register(Review)
