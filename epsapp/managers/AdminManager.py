from django.contrib.auth.models import BaseUserManager


class AdminManager(BaseUserManager):
    def create_user(self, username, password, name=None, phone=None, email=None, dob=None, status=None, login=None, logout=None, password2=None):
        if not username:
            raise ValueError("Username is Required !!!")

        admin = self.model(
            name=name,
            phone=phone,
            email=email,
            dob=dob,
            username=username,
            status=status,
            login=login,
            logout=logout
        )
        admin.set_password(password)
        admin.save(using=self._db)
        return admin

    # Create Super User Here
    def create_superuser(self, username, password, name=None, phone=None, email=None, dob=None, status=None, login=None, logout=None):
        admin = self.create_user(
            username=username,
            password=password,
            name=name,
            phone=phone,
            email=email,
            dob=dob,
            status=status,
            login=login,
            logout=logout
        )
        admin.is_admin = True
        admin.save(using=self._db)
        return admin
