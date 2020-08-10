from .models import User

class Auth:
    def authenticate(self, username=None, password=None):
        try:
            user = User.objects.get(username=username)
            return user
        except:
            return None

    def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except:
            return None