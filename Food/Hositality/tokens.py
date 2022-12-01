from django.contrib.auth.tokens import PasswordResetTokenGenerator

from six import text_type


class TokenGenerator(PasswordResetTokenGenerator):
    def _make_hash_value(self, user, timestramp):
        return (text_type(user.pk) + text_type(timestramp))


Generate_Token = TokenGenerator()