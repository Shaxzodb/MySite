from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls.i18n import i18n_patterns
from django.contrib import sitemaps
from Articles.models import ArticleModel
from Channels.models import Channel
from django.urls import reverse
from django.contrib.sitemaps import views as sitemaps_views
from django.views.decorators.cache import cache_page
from App.views import robots
# from App.admin import admin_site

class StaticViewSitemap(sitemaps.Sitemap):
    changefreq = "weekly"
    priority = 0.9
    i18n = True
    
    def items(self):
        return ['homepage','list']
    
    def location(self, item):
        return reverse(item)
    
class ArticleDetailViewSitemap(sitemaps.Sitemap):
    changefreq = "always"
    priority = 1.0
    i18n = True
    limit = 50000 #default 50000
    
    def items(self):
        return ArticleModel.objects.all()
    
    def lastmod(self, obj):
        return obj.updated_at
    
class ChannelDetailViewSitemap(sitemaps.Sitemap):
    changefreq = "always"
    priority = 1.0
    i18n = True
    limit = 50000 #default 50000
    
    def items(self):
        return Channel.objects.all()
    
    def lastmod(self, obj):
        return obj.updated_ch

sitemaps = {
    'static': StaticViewSitemap,
    'article-detail': ArticleDetailViewSitemap,
    'channel-detail': ChannelDetailViewSitemap
}

urlpatterns = [
    path('__debug__/', include('debug_toolbar.urls')),
    
    path('i18n/', include('django.conf.urls.i18n')),
    path('robots.txt',robots),
    path('sitemap.xml',
        cache_page(86400)(sitemaps_views.index),
        {'sitemaps': sitemaps, 'sitemap_url_name': 'sitemaps'},
    ),
    path('sitemap-<section>.xml',
        cache_page(86400)(sitemaps_views.sitemap),
        {'sitemaps': sitemaps}, name='sitemaps'
    ),
    path('hitcount/', include(('hitcount.urls', 'hitcount'), namespace='hitcount')),
    path("ckeditor5/", include('django_ckeditor_5.urls')),
] + i18n_patterns(
    #path('accounts/', include('allauth.urls')),
    path('admin/', admin.site.urls),
    # path('special/admin/', admin_site.urls),
    path('',include('App.urls')),
    # path('',include('APIs.urls')),
    path('',include('Users.urls')),
    path('',include('Channels.urls')),
    path('',include('Articles.urls')),
    path('',include('Comments.urls')),
    path('register/', include('django.contrib.auth.urls')),
) + static(
    settings.MEDIA_URL, document_root=settings.MEDIA_ROOT
) + static(
    settings.STATIC_URL, document_root=settings.STATIC_ROOT
)