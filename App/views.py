from django.shortcuts import render
from django_ratelimit.decorators import ratelimit
from django.utils.translation import gettext as _

# Create your views here.
@ratelimit(key='ip', rate='100/5m')
def Homepage(request):
    template_name = 'index.html'
    output = _("Ha Bu Ajoyib bo'ldi")
    return render(request, template_name, context={})

def Ratelimited(request):
    template_name = '403.html'
    return render(request, template_name)
   