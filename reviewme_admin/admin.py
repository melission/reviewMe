from django.contrib import admin
from django.template.response import TemplateResponse
from django.urls import path


# Register your models here.
class ReviewMeAdmin(admin.AdminSite):
    site_header = 'ReviewMe // Administration Side'
    logout_template = 'admin/logout.html'

    def profile_view(self, request):
        request.current_app = self.name
        context = self.each_context(request)
        return TemplateResponse(request, 'admin/admin_profile.html', context)


admin_site = ReviewMeAdmin(name='reviewme_admin')