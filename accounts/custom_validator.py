from django.core.exceptions import ValidationError
from django.contrib.auth.password_validation import \
    UserAttributeSimilarityValidator


class CustomPasswordMinLength(object):
    """check if password is 14 characters or more """

    def validate(self, password, user=None):
        if len(password) < 14:
            raise ValidationError(
                'Password must be longer then 14 characters.')

    def get_help_text(self):
        return "Password must be longer then 14 characters."


class CustomSamePassword(UserAttributeSimilarityValidator):
    """check if password matches the old one and also
     if password contains personal detials """

    def validate(self, password, user=None):
        if user:
            if user.check_password(password):
                raise ValidationError(
                    'Password cannot be the same as the old one.')
            if user.get_short_name():
                if user.get_short_name().lower() in password.lower():
                    raise ValidationError(
                        'Password cannot be apart of your first name.')
            if user.last_name:
                if user.last_name.lower() in password.lower():
                    raise ValidationError(
                        'Password cannot be apart of your last name.')
            if user.get_username():
                if user.get_username().lower() in password.lower():
                    raise ValidationError(
                        'Password cannot be apart of your username.')

    def get_help_text(self):
        return "Password cannot match your old one or be apart of any" \
               " personal details"


class CustomOneNumber(object):
    """check is password contains one number """

    def validate(self, password, user=None):
        # check for digit
        if not any(char.isdigit() for char in password):
            raise ValidationError('Password must contain at least 1 digit.')

    def get_help_text(self):
        return "Password must contain at least 1 digit."


class CustomOneUpperCase(object):
    """check if password contains one uppercase letter"""

    def validate(self, password, user=None):
        # check for letter
        if not any(char.isupper() for char in password):
            raise ValidationError(
                'Password must contain one uppercase letter.')

    def get_help_text(self):
        return "Password must contain one uppercase letter."


class CustomOneLowerCase(object):
    """check if password contains one lowercase letter"""

    def validate(self, password, user=None):
        if not any(char.islower() for char in password):
            raise ValidationError(
                'Password must contain one lowercase letter.')

    def get_help_text(self):
        return "Password must contain one lowercase letter."


class CustomOneSpecialCharacter(object):
    """check if password contains one special character"""

    def validate(self, password, user=None):
        # check for special character
        special_characters = "[~\!@#\$%\^&\*\(\)_\+{}\":;'\[\]]"
        if not any(char in special_characters for char in password):
            raise ValidationError('Password must contain 1 special character')

    def get_help_text(self):
        return "Password must contain 1 special character"
