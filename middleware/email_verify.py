from Users.models import CustomUserModel
from django.shortcuts import get_object_or_404

class EmailVerification:
    
    def __init__(self, get_response):
        self.get_response = get_response
        # One-time configuration and initialization.

    def __call__(self, request):
        # Code to be executed for each request before
        # the view (and later middleware) are called.
        response = self.get_response(request)
        return response
    def process_template_response(self, request, response):
        if request.user.is_authenticated:
            user = get_object_or_404(CustomUserModel, id = request.user.id)
            response.context_data['email_verification'] = user.email_verification
        return response

