from django.contrib.auth.backends import ModelBackend
from django.contrib.auth.models import User
# from .models import User


class EmailAuth:
    def authenticate(self, request, email, password):
        try:
            user = User.objects.get(email=email)
            success = user.check_password(password)
            if success:
                return user
        except User.DoesNotExist:
            pass
        return None

    def get_user(self, uid):
        try:
            return User.objects.get(pk=uid)
        except:
            return None

