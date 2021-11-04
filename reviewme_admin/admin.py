from django.contrib import admin


# Register your models here.
class ReviewMeAdmin(admin.AdminSite):
    site_header = 'ReviewMe // Administration Side'
    logout_template = 'admin/logout.html'


admin_site = ReviewMeAdmin(name='reviewme_admin')