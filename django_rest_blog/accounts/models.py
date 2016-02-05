from django.db import models

from authemail.models import EmailUserManager, EmailAbstractUser

class RestEmailUser(EmailAbstractUser):

    # Required
    objects = EmailUserManager()