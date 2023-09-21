"""Test for This application."""
import datetime

from django.test import TestCase
from django.utils import timezone
import django.test
from django.urls import reverse
from django.contrib.auth.models import User
from polls.models import Question, Choice
from mysite import settings


class QuestionModelTests(TestCase):
    """Test for Question model."""

    def test_was_published_recently_with_future_question(self):
        """Returns False if question's publication is in the future."""
        time = timezone.localtime(timezone.now()) + datetime.timedelta(days=30)
        future_question = Question(pub_date=time)
        self.assertIs(future_question.was_published_recently(), False)

    def test_was_published_recently_with_old_question(self):
        """Returns False if question's pub_date is more than 1 day old."""
        time = timezone.localtime(timezone.now())
        - datetime.timedelta(days=1, seconds=1)
        old_question = Question(pub_date=time)
        self.assertIs(old_question.was_published_recently(), False)

    def test_was_published_recently_with_recent_question(self):
        """Returns True for questions within last day's pub_date."""
        time = timezone.localtime(timezone.now())
        - datetime.timedelta(hours=23, minutes=59, seconds=59)
        recent_question = Question(pub_date=time)
        self.assertIs(recent_question.was_published_recently(), True)

    def test_question_with_future_pub_date(self):
        """is_published returns False for questions with future pub_date."""
        time = timezone.localtime(timezone.now()) + datetime.timedelta(days=1)
        future_question = Question(pub_date=time)
        self.assertIs(future_question.is_published(), False)

    def test_question_with_default_pub_date(self):
        """is_published returns True for questions with default pub_date."""
        question = Question(question_text="What")
        question.save()
        self.assertIs(question.is_published(), True)

    def test_question_with_pub_date_in_the_past(self):
        """is_published returns True for questions with past pub_date."""
        time = timezone.localtime(timezone.now()) - datetime.timedelta(days=2)
        past_question = Question(pub_date=time)
        self.assertIs(past_question.is_published(), True)

    def test_question_with_no_end_date(self):
        """can_vote returns True for questions with no end_date."""
        time = timezone.localtime(timezone.now()) - datetime.timedelta(days=20)
        question_no_end_date = Question(pub_date=time)
        self.assertIs(question_no_end_date.can_vote(), True)

    def test_can_vote_between_published_date_and_end_date(self):
        """can_vote returns True between published and end date."""
        time_pub_date = timezone.localtime(timezone.now())
        time_end_date = timezone.localtime(timezone.now())
        + datetime.timedelta(days=1)
        question_btw_pub_and_end_date = Question(pub_date=time_pub_date,
                                                 end_date=time_end_date)
        self.assertIs(question_btw_pub_and_end_date.can_vote(), True)

    def test_can_not_vote_before_published_date(self):
        """can_vote returns False for questions not yet published."""
        time_pub_date = timezone.localtime(timezone.now())
        + datetime.timedelta(days=1)
        question_before_pub_date = Question(pub_date=time_pub_date)
        self.assertEqual(question_before_pub_date.can_vote(), False)

    def test_can_not_vote_after_end_date(self):
        """can_vote returns False for questions already ended."""
        time_pub_date = timezone.localtime(timezone.now())
        - datetime.timedelta(days=2)
        time_end_date = timezone.localtime(timezone.now())
        - datetime.timedelta(days=1)
        question_after_end_date = Question(pub_date=time_pub_date,
                                           end_date=time_end_date)
        self.assertIs(question_after_end_date.can_vote(), False)


def create_question(question_text, days):
    """Create question with `question_text` and publish `days` from now."""
    time = timezone.localtime(timezone.now()) + datetime.timedelta(days=days)
    return Question.objects.create(question_text=question_text, pub_date=time)


class QuestionIndexViewTests(TestCase):
    """Test for question in index view."""
    def test_no_questions(self):
        """If no questions exist, an appropriate message is displayed."""
        response = self.client.get(reverse('polls:index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "No polls are available.")
        self.assertQuerysetEqual(response.context['latest_question_list'], [])

    def test_past_question(self):
        """Displays past questions with a pub_date on the index page."""
        question = create_question(question_text="Past question.", days=-30)
        response = self.client.get(reverse('polls:index'))
        self.assertQuerysetEqual(
            response.context['latest_question_list'],
            [question],
        )

    def test_future_question(self):
        """Questions in the future aren't displayed on the index page."""
        time = timezone.localtime(timezone.now()) + datetime.timedelta(days=30)
        Question(question_text="Future question.", pub_date=time)
        response = self.client.get(reverse('polls:index'))
        self.assertContains(response, "No polls are available.")
        self.assertQuerysetEqual(response.context['latest_question_list'], [])

    def test_future_question_and_past_question(self):
        """Only past questions are displayed."""
        question = create_question(question_text="Past question", days=-30)
        create_question(question_text="Future question.", days=+30)
        response = self.client.get(reverse('polls:index'))
        self.assertQuerysetEqual(
            response.context['latest_question_list'],
            [question],
        )

    def test_two_past_questions(self):
        """The questions index page may display multiple questions."""
        question1 = create_question(question_text="Past question 1.", days=-30)
        question2 = create_question(question_text="Past question 2.", days=-5)
        response = self.client.get(reverse('polls:index'))
        self.assertQuerysetEqual(
            response.context['latest_question_list'],
            [question2, question1],
        )

    def test_past_question_in_detail_view(self):
        """The detail view of a past question displays the question's text."""
        past_question = create_question(question_text='Past Question.',
                                        days=-5)
        url = reverse('polls:detail', args=(past_question.id,))
        response = self.client.get(url)
        self.assertContains(response, past_question.question_text)


class UserAuthTest(django.test.TestCase):
    """Test for User authentication."""

    def setUp(self):
        """Creates a Client object and initializes test database."""
        super().setUp()
        self.username = "testuser"
        self.password = "FatChance!"
        self.user1 = User.objects.create_user(
                         username=self.username,
                         password=self.password,
                         email="testuser@nowhere.com"
                         )
        self.user1.first_name = "Tester"
        self.user1.save()
        # we need a poll question to test voting
        q = Question.objects.create(question_text="First Poll Question")
        q.save()
        # a few choices
        for n in range(1, 4):
            choice = Choice(choice_text=f"Choice {n}", question=q)
            choice.save()
        self.question = q

    def test_logout(self):
        """A user can logout using the logout url.

        As an authenticated user,
        when I visit /accounts/logout/
        then I am logged out
        and then redirected to the login page.
        """
        logout_url = reverse("logout")
        # Authenticate the user.
        # We want to logout this user, so we need to associate the
        # user user with a session.  Setting client.user = ... doesn't work.
        # Use Client.login(username, password) to do that.
        # Client.login returns true on success
        self.assertTrue(
              self.client.login(username=self.username, password=self.password)
                       )
        # visit the logout page
        response = self.client.get(logout_url)
        self.assertEqual(302, response.status_code)

        # should redirect us to where? Polls index? Login?
        self.assertRedirects(response, reverse(settings.LOGOUT_REDIRECT_URL))

    def test_login_view(self):
        """A user can login using the login view."""
        login_url = reverse("login")
        # Can get the login page
        response = self.client.get(login_url)
        self.assertEqual(200, response.status_code)
        # Can login using a POST request
        form_data = {"username": "testuser",
                     "password": "FatChance!"}
        response = self.client.post(login_url, form_data)
        # after successful login, should redirect browser somewhere
        self.assertEqual(302, response.status_code)
        # should redirect us to the polls index page ("polls:index")
        self.assertRedirects(response, reverse(settings.LOGIN_REDIRECT_URL))

    def test_auth_required_to_vote(self):
        """Authentication is required to submit a vote.

        As an unauthenticated user,
        when I submit a vote for a question,
        then I am redirected to the login page
        or I receive a 403 response (FORBIDDEN)
        """
        vote_url = reverse('polls:vote', args=[self.question.id])

        # What choice to vote for?
        choice = self.question.choice_set.first()
        # The polls detail page has a form, each choice is identified by its id
        form_data = {"choice": f"{choice.id}"}
        response = self.client.post(vote_url, form_data)

        # Should be redirected to the login page
        self.assertEqual(response.status_code, 302)
        login_url = reverse('login')
        expected_login_url = f"{login_url}?next={vote_url}"
        self.assertRedirects(response, expected_login_url)
