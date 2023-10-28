"""This module defines the models for the polls application."""
from django.db import models
from .question import Question

class Choice(models.Model):
    """Represents a choice for a poll question.

    Attributes:
        question (Question): The question associated with this choice.
        choice_text (str): The text of the choice.
        votes (int): The number of votes received for this choice.
    """
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)

    @property
    def votes(self):
        """Compute the number of votes received for this choice."""
        return self.vote_set.count()

    def __str__(self):
        """Returns a string representation of the choice text."""
        return self.choice_text
