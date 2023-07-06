# from django.contrib.auth.models import User
from polling.users.models import User
from rest_framework import authentication
from rest_framework import exceptions


class EmailAuthentication(authentication.BaseAuthentication):
    def authenticate(self, request, **kwargs):
        email = kwargs.get('email', None)
        if email is None:
            return None

        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            raise exceptions.AuthenticationFailed('No user found with given email!')

        return (user, None)
