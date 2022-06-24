from django.core.exceptions import ValidationError

def validate_indeks_nilai(value):
    val = value
    if val > 50 :
        message = 'Sorry, ' + str(val) + ' is exceeds the maximum score'
        raise ValidationError(message)