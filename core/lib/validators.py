from django.core.exceptions import ValidationError


def bmi_validate(value):
    if 5 > value > 100:
        raise ValidationError('please enter bmi between 5 - 100')

def general_health_validate(value):
    if 1 > value > 5:
        raise ValidationError('please enter number between 1-5')

def mental_physical_health_validate(value):
    if 0 > value > 30:
        raise ValidationError('please enter number between 1-5')

def age_validate(value):
    if 18 > value:
        raise ValidationError('please enter number between 1-5')

