"""This module defines the models for the polls application."""
import datetime
from django.db import models
from django.utils import timezone


class Question(models.Model):
    """Represents a question that can be asked in a poll.

    Attributes:
        question_text (str): The text of the question.
        pub_date (datetime.datetime): published date and published time.
        end_date (datetime.datetime, optional): end date and end time.
    """
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published', default=timezone.now)
    end_date = models.DateTimeField('end date', null=True, blank=True)

    def __str__(self):
        """Returns a string representation of the question text.

        :return: question_text
        """
        return self.question_text

    def was_published_recently(self):
        """Checks if the question was published recently in 1 day.

        :return: bool: True if the question was published, False otherwise.
        """
        now = timezone.localtime(timezone.now())
        return now - datetime.timedelta(days=1) <= self.pub_date <= now

    def is_published(self):
        """Checks if the current date is on or after publication date.

        return: bool: True if the question is published, False otherwise.
        """
        return self.pub_date <= timezone.localtime(timezone.now())

    def can_vote(self):
        """Checks if voting is allowed for this question.

        return: bool: True if users can vote on the question, False otherwise.
        """
        now = timezone.localtime(timezone.now())
        if self.end_date is None and now >= self.pub_date:
            return True
        return self.pub_date <= now and now < self.end_date
    