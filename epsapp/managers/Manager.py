from django.contrib.auth.models import BaseUserManager


class UserManager(BaseUserManager):
    def create_user(self, username, password, user_type=None, organization=None, password2=None):
        if not username:
            raise ValueError("Username is Required !!!")

        users = self.model(
            organization=organization,
            username=username,
            user_type=user_type,
        )
        users.set_password(password)
        users.save(using=self._db)
        return users

    # Create Super User Here
    def create_superuser(self, username, password, user_type=1, organization=None):
        users = self.create_user(
            username=username,
            password=password,
            user_type=user_type,
            organization=organization,
        )
        users.is_admin = True
        users.save(using=self._db)
        return users
