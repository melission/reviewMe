from django.contrib import admin


# Register your models here.
class ReviewMeAdmin(admin.AdminSite):
    site_header = 'ReviewMe // Administration Side'


admin_site = ReviewMeAdmin(name='reviewme_admin')