from .models import CustomUser


class EmailIdNumberAuthBackend:
    """
    Custom authentication backend.

    Allows users to log in using their email address and id number.
    """

    def authenticate(self, request, email=None, id_number=None):
        """
        Overrides the authenticate method to allow users to log in using their email address.
        """
        try:
            user = CustomUser.objects.get(email=email)
            if user.id_number == id_number:
                return user
            return None
        except CustomUser.DoesNotExist:
            return None

    def get_user(self, user_id):
        """
        Overrides the get_user method to allow users to log in using their email address.
        """
        try:
            return CustomUser.objects.get(pk=user_id)
        except CustomUser.DoesNotExist:
            return None
