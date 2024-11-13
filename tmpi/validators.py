from django.core.exceptions import ValidationError

def validate_excel_file(value):
    limit = 1 * 1024 * 1024
    if value.size > limit :
        message = 'File too large. Size should not exceed 1 MiB.'
        raise ValidationError(message)

def validate_extension(value):
    ext = '.xlsx'
    if value.lower().endswith(('.xlsx')) != ext :
        message = 'Please upload excel file.'
        raise ValidationError(message)