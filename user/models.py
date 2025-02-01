from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models


class CustomUser(AbstractUser):
    phone_number = models.CharField(max_length=15, blank=True, null=True)

    # related_nameを設定して競合を回避
    groups = models.ManyToManyField(
        Group,
        related_name='customuser_set',  # 適当な名前を設定
        blank=True
    )
    user_permissions = models.ManyToManyField(
        Permission,
        related_name='customuser_permissions_set',  # 適当な名前を設定
        blank=True
    )
