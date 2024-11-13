from django.core.exceptions import ValidationError

def validate_image(value):
    limit = 0.5 * 1024 * 1024
    if value.size > limit :
        message = 'File too large. Size should not exceed 500 KB.'
        raise ValidationError(message)