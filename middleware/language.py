from django.utils import translation
from django.conf import settings

def LocaleMiddleware(get_response):
    # One-time configuration and initialization.

    def middleware(request):
        # Code to be executed for each request before
        # the view (and later middleware) are called.

        response = get_response(request)
        user_language = translation.get_language()
        translation.activate(user_language)
        response.set_cookie(
            settings.LANGUAGE_COOKIE_NAME, 
            user_language
        )
        # Code to be executed for each request/response after
        # the view is called.

        return response

    return middleware
