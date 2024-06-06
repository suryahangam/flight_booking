from django.db import models
from django.contrib.auth.models import (AbstractBaseUser, 
                                        BaseUserManager, PermissionsMixin)


class UserManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, email, password, **extra_fields):
        """
        Creates and saves a User with the given email and password.
        """
        if not email:
            raise ValueError('The given email must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(email, password, **extra_fields)


# Abstract User
class CustomUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=True)
    date_joined = models.DateTimeField(auto_now_add=True)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email

    def get_user_type(self):
        pass  # Implement as needed


# Profile
class Profile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    contact_number = models.CharField(max_length=15)
    dob = models.DateField()
    loyalty_member_id = models.CharField(max_length=50)
    preferred_language = models.CharField(max_length=50)
    coverage_area = models.CharField(max_length=255)


# Passenger
class Passenger(models.Model):
    full_name = models.CharField(max_length=255)    
    passport_number = models.CharField(max_length=50)
    date_of_birth = models.CharField(max_length=50, null=True)
    special_needs = models.CharField(max_length=255, null=True)
    frequent_flyer_number = models.CharField(max_length=50, null=True)


# Notification
class Notification(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    message = models.CharField(max_length=500)
    notification_type = models.CharField(max_length=50)
    date_sent = models.DateTimeField()
    notification_subject = models.CharField(max_length=255)

