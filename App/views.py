from django.shortcuts import render
from django.core.mail import send_mail
from django_ratelimit.decorators import ratelimit
from django.utils.translation import gettext as _
# Create your views here.
import logging
from asgiref.sync import sync_to_async
from django.shortcuts import get_object_or_404
from Users.models import CustomUserModel
from django.http import Http404
from django.conf import settings

from django.template import Context, loader
from django.utils import translation
from django.http import HttpResponse

@ratelimit(key='ip', rate='30/m')
@ratelimit(key='post:username',rate='30/m')
def Base(request):
    # try:
    #     email_template = loader.render_to_string('accounts/print.html')
    #     send_mail(
    #     'Salom Shaxzod',
    #     #'Salom Shaxzod',
    #     None,
    #     settings.EMAIL_HOST_USER,
    #     ('shaxzodbmaster@gmail.com',),
       
    #     fail_silently=False,
    #     html_message=email_template,
    # )
    # except:
    #user = User.objects.get(username="Admins")
    try:
        passuser = 23#get_object_or_404(CustomUserModel,pk=request.user.pk)
    except :
        raise Http404("Given query not found....")
    output = _("HA Bu Ajoyib bo'ldi")
    user_language = translation.get_language()

    translation.activate(user_language)
    response = render(request,'index.html',context={'pss':passuser,'til':output})
    response.set_cookie(settings.LANGUAGE_COOKIE_NAME, user_language)
    
    return response
   