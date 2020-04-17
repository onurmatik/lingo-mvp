from django.db import models
from django.contrib.auth.models import User
from django.conf import settings


class Meeting(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
    )
    language = models.CharField(
        max_length=10,
        choices=settings.LANGUAGES
    )
    time = models.DateTimeField()
    meeting_url = models.URLField()
    password = models.CharField(
        max_length=20,
        blank=True, null=True
    )
