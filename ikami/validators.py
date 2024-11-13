from django.core.exceptions import ValidationError

def validate_tata_kelola(value):
    limit = 126
    if value > limit :
        message = 'Value exceeds limit'
        raise ValidationError(message)

def validate_pengelolaan_risiko(value):
    limit = 72
    if value > limit :
        message = 'Value exceeds limit'
        raise ValidationError(message)

def validate_kerangka_kerja(value):
    limit = 159
    if value > limit :
        message = 'Value exceeds limit'
        raise ValidationError(message)

def validate_pengelolaan_aset(value):
    limit = 168
    if value > limit :
        message = 'Value exceeds limit'
        raise ValidationError(message)

def validate_teknologi_keamanan(value):
    limit = 120
    if value > limit :
        message = 'Value exceeds limit'
        raise ValidationError(message)