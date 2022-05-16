"""reviewMe URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views
from . import api_views
from pdf_generator.views import pdf_template
from reviewme_admin.admin import admin_site

router = DefaultRouter()
router.register(r'books', api_views.AllBookViewSet)
router.register(r'book_reviews', api_views.ReviewBookViewSet)
router.register(r'movies', api_views.AllMovieViewSet)
urlpatterns = [
    path('api/', include((router.urls, 'api'))),
    path('api/login', api_views.Login.as_view(), name='login'),
    path('admin/', admin.site.urls),
    # path('api/all_books', api_views.AllBookViewSet.as_view()),
    # path('api/contributors', api_views.ContributorView.as_view()),
    path('accounts/', include(('django.contrib.auth.urls', 'auth'), namespace='accounts')),
    path('accounts/profile/', views.profile, name='profile'),
    path('', views.index, name='main_page'),
    path('search/', views.searchField),
    path('books/', include('books.urls')),
    path('movies/', include('movies.urls')),
    # the path below is for testing purposes only
    path('pdf_template', pdf_template)
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
