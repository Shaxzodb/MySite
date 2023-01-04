from django.shortcuts import render
from django.utils.translation import gettext as _
from django.views.generic import TemplateView
from django.contrib.sites.models import Site

# Create your views here.
class Homepage(TemplateView):
    template_name = 'homepage.html'
    def get(self, *args, **kwargs):
        context = super().get(self, *args, **kwargs)
        return context
    
def rate_limited(request):
    template_name = '429.html'
    return render(request, template_name)

def robots(request):
    template_name="bots/robots.txt",
    current_site = Site.objects.get_current()
    return render(request, template_name, content_type="text/plain", context={'site_domain':current_site})
   