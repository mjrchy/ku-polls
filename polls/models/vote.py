from django.db import models
from .choice import Choice
from django.contrib.auth.models import User

class Vote(models.Model):
    """Records a Vote of a Choice by a User."""
    choice = models.ForeignKey(Choice, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        """A string representing the user's vote for a choice."""
        return str(self.user) + " voted for " + str(self.choice)
