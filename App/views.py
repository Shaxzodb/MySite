from django.shortcuts import render
from django.contrib.sites.models import Site
from middleware.language import LocaleMiddleware
from django.shortcuts import get_object_or_404
from Users.models import CustomUserModel
# Create your views here.
    
@LocaleMiddleware
def base(request):
    email_verification = True
    template_name = 'base.html'
    if request.user.is_authenticated:
        user = get_object_or_404(CustomUserModel, id = request.user.id)
        email_verification = user.email_verification
    return render(request, template_name ,{'email_verification':email_verification})
    
@LocaleMiddleware
def about(request):
    email_verification = True
    template_name = 'about.html'
    if request.user.is_authenticated:
        user = get_object_or_404(CustomUserModel, id = request.user.id)
        email_verification = user.email_verification
    return render(request, template_name ,{'email_verification':email_verification})

def rate_limited(request):
    template_name = '429.html'
    return render(request, template_name)

def robots(request):
    template_name="bots/robots.txt",
    current_site = Site.objects.get_current()
    return render(request, template_name, content_type="text/plain", context={'site_domain':current_site})
   