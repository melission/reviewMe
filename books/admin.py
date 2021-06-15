from django.contrib import admin
from .models import *
from reviewMe.admin import *
# Register your models here.


class BookAdmin(admin.ModelAdmin):
    date_hierarchy = 'published_at'
    list_display = ('title', 'isnb_with_dashes', 'published_at')
    list_filter = ('publisher', 'contributors', 'published_at',)
    search_fields = ('title', 'isbn', 'contributors')
    # filter = () // to modify the fields users will see in the admin panel
    # fieldsets = (('The title and contributors', {'fields': ('title',)}),
    #              ('Info', {'fields': ('publisher', 'description')})
    #              # two tuples value only
    #              )

    def isnb_with_dashes(self, obj):
        """ '9780316769174' => '978-0-31-676917-4' """
        return '{}-{}-{}-{}-{}'.format(
            obj.isbn[0:3], obj.isbn[3:4], obj.isbn[4:6], obj.isbn[6:12], obj.isbn[12:13])


class ContributorAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name')
    list_filter = ('last_name',)
    search_fields = ('first_name', 'last_name')


admin.site.register(Publisher)
admin.site.register(Contributor, ContributorAdmin)
admin.site.register(Book, BookAdmin)
admin.site.register(BookContributor)
admin.site.register(Review)
