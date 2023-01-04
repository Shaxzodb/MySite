from django.core.exceptions import ValidationError

def validate_length(value,length=6):
    if len(str(value))<=length:
        raise ValidationError(f'{value} is not the correct length')