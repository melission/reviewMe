from django.contrib import admin
# from django.contrib.admin import AdminSite


class ReviewMeConfig(admin.AdminSite):
    title_header = 'ReviewMe'
    site_header = 'ReviewMe administration'
    index_title = 'ReviewMe site admin'
