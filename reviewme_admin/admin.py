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

    # this function overrides a custom get_urls()
    def get_urls(self):
        # fetches the list of urls that mapped to the admin class
        urls = super().get_urls()

        # needs to map a custom view to a url provided by the admin site.
        url_patterns = [path("admin_profile", self.admin_view(self.profile_view))]
        # print(urls)
        # print(url_patterns)

        # url_patterns must be returned at a first variable,
        # otherwise Django mapping cannot find path to 'admin/admin_profile
        return url_patterns + urls


admin_site = ReviewMeAdmin(name='reviewme_admin')
