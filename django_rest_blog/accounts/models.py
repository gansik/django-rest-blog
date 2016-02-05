#from django.conf import settings
from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser
from rest_framework.authtoken.models import Token



'''	Base on https://docs.djangoproject.com/en/1.9/topics/auth/customizing/
'''
class RestEmailUserManager(BaseUserManager):
    def create_user(self, email, password=None):
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            email=self.normalize_email(email),
        )

        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, password):

        user = self.create_user(email,
            password=password,
        )
        user.is_admin = True
        user.save(using=self._db)
        return user

class RestEmailUser(AbstractBaseUser):
    email = models.EmailField(
        verbose_name='email address',
        max_length=255,
        unique=True,
    )

    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    objects = RestEmailUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    @property
    def is_staff(self):
        return self.is_admin

    def get_full_name(self):
        return self.email

    def get_short_name(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return self.is_admin

    def __str__(self):
        return self.email

    def set_token(self):
        Token.objects.create(user=self)

    def save(self, *args, **kwargs):

        is_new = self.pk is None

        super(RestEmailUser, self).save(*args, **kwargs)

        if is_new:	# create token for new user
            self.set_token()


"""
#from django.db.models.signals import post_save
#from django.dispatch import receiver

@receiver(post_save, sender=RestEmailUser)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        instance.set_token()
"""
