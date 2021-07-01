import re

from django.core.exceptions import ValidationError
from django.utils.translation import ugettext as _


class NumberValidator(object):
    def __init__(self, min_digits=0):
        self.min_digits = min_digits

    def validate(self, password):
        if not len(re.findall('\d', password)) >= self.min_digits:
            raise ValidationError(
                _("The password must contain at least %(min_digits)d digit(s), 0-9."),
                code='password_no_number',
                params={'min_digits': self.min_digits},
            )

    def get_help_text(self):
        return _(
            "Your password must contain at least 1 digit, 0-9." % {'min_digits': self.min_digits}
        )


class UppercaseValidator(object):
    def __init__(self, min_upper_case=0):
        self.min_upper_case = min_upper_case

    def validate(self, password, user=None):
        if not len(re.findall('\d', password)) >= self.min_upper_case:
            raise ValidationError(
                _("The password must contain at least 1 uppercase letter, A-Z."),
                code='password_no_upper',
                params={'min_upper_case': self.min_upper_case},

            )

    def get_help_text(self):
        return _(
            "Your password must contain at least 1 uppercase letter, A-Z."
        )

'''
class LowercaseValidator(object):
    def __init__(self, min_lower_case=0):
        self.min_lower_case = min_lower_case

    def validate(self, password):
        if not len(re.findall('\d', password)) >= self.min_lower_case:
            raise ValidationError(
                _("The password must contain at least 1 lowercase letter, a-z."),
                code='password_no_lower',
                params={'min_lower_case': self.min_lower_case},

            )

    def get_help_text(self):
        return _(
            "Your password must contain at least 1 lowercase letter, a-z."
        )


class SymbolValidator(object):
    def __init__(self, min_symbol=0):
        self.min_symbol = min_symbol

    def validate(self, password):
        if not len(re.findall('\d', password)) >= self.min_symbol:
            raise ValidationError(
                _("The password must contain at least 1 symbol: " +
                  "()[]{}|\`~!@#$%^&*_-+=;:'\",<>./?"),
                code='password_no_symbol',
                params={'min_symbol': self.min_symbol},

            )

    def get_help_text(self):
        return _(
            "Your password must contain at least 1 symbol: " +
            "()[]{}|\`~!@#$%^&*_-+=;:'\",<>./?"
        )
'''