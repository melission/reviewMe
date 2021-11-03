from django.apps import AppConfig
from django.contrib.admin.apps import AdminConfig


# the child class that overwrites 'default_site' properties and allows to register all models.
class ReviewmeAdminConfig(AdminConfig):
    # default_auto_field = 'django.db.models.BigAutoField'
    # name = 'reviewme_admin'
    default_site = 'reviewme_admin.admin.ReviewMeAdmin'
