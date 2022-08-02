from django.db import models
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser
)


class UserManager(BaseUserManager):
    def create_user(self, username, role, password=None):
        """
        Creates and saves a User with the given email, date of
        birth and password.
        """
        if not username:
            raise ValueError('Username must be provided')

        user = self.model(
            username=username,
            role=role,
        )

        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password=None):
        """
        Creates and saves a superuser with the given email, date of
        birth and password.
        """
        user = self.create_user(
            email,
            password=password,
            role=1,
        )
        user.save()
        return user


RolesChoices = [
    (1, "LIBRARIAN"),
    (2, "MEMBER")
]


class User(AbstractBaseUser):
    USERNAME_FIELD = 'username'
    username = models.CharField(
        max_length=255,
        unique=True,
        null=False,
    )
    role = models.IntegerField(default=RolesChoices, choices=RolesChoices)
    objects = UserManager()