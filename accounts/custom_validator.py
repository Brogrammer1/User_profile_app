from django.core.exceptions import ValidationError


class CustomPasswordMinLength(object):

    def validate(self, password, user=None):
        if len(password) < 14:
            raise ValidationError(
                'Password must be longer then 14 characters.')

    def get_help_text(self):
        return "Password must be longer then 14 characters."


class CustomSamePassword(object):

    def validate(self, password, user=None):
        if user:
            if user.check_password(password):
                raise ValidationError(
                    'Password cannot be the same as the old one.')

    def get_help_text(self):
        return "Password cannot match your old one(for existing users only)"


class CustomOneNumber(object):

    def validate(self, password, user=None):
        # check for digit
        if not any(char.isdigit() for char in password):
            raise ValidationError('Password must contain at least 1 digit.')

    def get_help_text(self):
        return "Password must contain at least 1 digit."


class CustomOneUpperCase(object):

    def validate(self, password, user=None):
        # check for letter
        if not any(char.isupper() for char in password):
            raise ValidationError(
                'Password must contain one uppercase letter.')

    def get_help_text(self):
        return "Password must contain one uppercase letter."


class CustomOneLowerCase(object):

    def validate(self, password, user=None):
        if not any(char.islower() for char in password):
            raise ValidationError(
                'Password must contain one lowercase letter.')

    def get_help_text(self):
        return "Password must contain one lowercase letter."


class CustomOneSpecialCharacter(object):

    def validate(self, password, user=None):
        # check for special character
        special_characters = "[~\!@#\$%\^&\*\(\)_\+{}\":;'\[\]]"
        if not any(char in special_characters for char in password):
            raise ValidationError('Password must contain 1 special character')

    def get_help_text(self):
        return "Password must contain 1 special character"
