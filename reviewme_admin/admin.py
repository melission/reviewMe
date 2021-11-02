from django.contrib import admin
from django.contrib.auth.admin import User


# Register your models here.
class ReviewMeAdmin(admin.AdminSite):
    site_header = 'ReviewMe // Administration Side'


admin_site = ReviewMeAdmin(name='reviewme_admin')
admin_site.register(User)