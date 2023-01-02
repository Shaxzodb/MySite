from django.shortcuts import render
from django.utils.translation import gettext as _
from django.views.generic import TemplateView

# Create your views here.
# def Homepage(request):
#     template_name = 'index.html'
#     output = _("Ha Bu Ajoyib bo'ldi")
    
#     return render(request, template_name, context={})
class Homepage(TemplateView):
    template_name = 'index.html'
    def get(self, *args, **kwargs):
        context = super().get(self, *args, **kwargs)
        return context
    
    
def ratelimited(request):
    template_name = '403.html'
    return render(request, template_name)
   