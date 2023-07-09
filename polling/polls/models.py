from django.db import models
from django.db.models import Avg
from polling.users.models import User
from polling.polls.utils import get_superuser


class Category(models.Model):
    name = models.CharField(max_length=40)

    def __str__(self):
        return self.name


class Poll(models.Model):
    title = models.CharField(max_length=40, unique=True)
    body = models.TextField(max_length=350, null=True, blank=True)
    is_public = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True, blank=True, null=True)
    category = models.ManyToManyField(Category, blank=True)
    creator = models.ForeignKey(User, on_delete=models.CASCADE, default=get_superuser)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return self.title

    @property
    def average_votes(self):
        return self.votes.aggregate(Avg("value"))["value__avg"]


class Vote(models.Model):
    value = models.PositiveSmallIntegerField(choices=[(i, i) for i in [1, 2, 3, 4, 5]], default=1)
    poll = models.ForeignKey(Poll, on_delete=models.CASCADE, related_name="votes")
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=["poll", "user"], name="unique_vote")
        ]
