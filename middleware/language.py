from django.utils import translation
from django.conf import settings

class LocaleMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        # One-time configuration and initialization.

    def __call__(self, request):
        # Code to be executed for each request before
        # the view (and later middleware) are called.

        response = self.get_response(request)
        user_language = translation.get_language()
        translation.activate(user_language)
        response.set_cookie(
            settings.LANGUAGE_COOKIE_NAME, 
            user_language
        )
        return response

