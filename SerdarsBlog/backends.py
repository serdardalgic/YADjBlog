from django.contrib.auth.models import User

from SerdarsBlog.models import UserProfile


class EmailAuthBackend(object):
    """
    Email Authentication Backend

    Allows a user to sign in using an email/password pair rather than
    a username/password pair.
    """

    def authenticate(self, username=None, password=None):
        """ Authenticate a user based on email address as the user name. """
        try:
            user = User.objects.get(email=username, is_active=True)
            if user.check_password(password):
                #TODO: Find a way to solve UserProfile.DoesNotExist problem
                #try:
                profile = UserProfile.objects.get(user=user)
                if profile.is_verified:
                    return user
                #except UserProfile.DoesNotExist:
                    #return user
            else:
                return None
        except User.DoesNotExist:
            return None

    def get_user(self, user_id):
        """ Get a User object from the user_id. """
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None
