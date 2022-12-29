"""Config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls.i18n import i18n_patterns
from django.views.generic import TemplateView
from django.contrib import sitemaps
from Articles.models import ArticleModel
from django.urls import reverse
from django.contrib.sitemaps import views as sitemaps_views
from django.views.decorators.cache import cache_page

class StaticViewSitemap(sitemaps.Sitemap):
    changefreq = "weekly"
    priority = 0.9
    i18n = True
    
    def items(self):
        return ['homepage','list']
    
    def location(self, item):
        return reverse(item)
    
class DetailViewSitemap(sitemaps.Sitemap):
    changefreq = "always"
    priority = 1.0
    i18n = True
    limit = 50000 #default 50000
    
    def items(self):
        return ArticleModel.objects.all()
    
    def lastmod(self, obj):
        return obj.updated_at
 
sitemaps = {
    'static': StaticViewSitemap,
    'detail': DetailViewSitemap
}

urlpatterns = [
    path('robots.txt',TemplateView.as_view(template_name="bots/robots.txt", content_type="text/plain")),
    path('sitemap.xml',
        cache_page(86400)(sitemaps_views.index),
        {'sitemaps': sitemaps, 'sitemap_url_name': 'sitemaps'},
    ),
    path('sitemap-<section>.xml',
        cache_page(86400)(sitemaps_views.sitemap),
        {'sitemaps': sitemaps}, name='sitemaps'
    ),
    path('hitcount/', include(('hitcount.urls', 'hitcount'), namespace='hitcount')),
] + i18n_patterns(
    path('admin/', admin.site.urls),
    path('',include('App.urls')),
    # path('',include('APIs.urls')),
    path('',include('Users.urls')),
    # path('',include('Profile.urls')),
    path('',include('Articles.urls')),
    # path('',include('Comments.urls')),
    path('registration/', include('django.contrib.auth.urls')),
    path('i18n/', include('django.conf.urls.i18n')),
    path("ckeditor5/", include('django_ckeditor_5.urls')),
) + static(
    settings.MEDIA_URL, document_root=settings.MEDIA_ROOT
) + static(
    settings.STATIC_URL, document_root=settings.STATIC_ROOT
)