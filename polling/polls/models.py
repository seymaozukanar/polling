from django.db import models


class Poll(models.Model):

    title = models.CharField(max_length=40, unique=True)
    body = models.TextField(max_length=350, null=True, blank=True)
    is_public = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True, blank=True, null=True)

    class Meta:
        ordering = ["-created_at"]
