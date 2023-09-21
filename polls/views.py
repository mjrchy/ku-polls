"""This module defines views and functions for the polls application."""
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic
from .models import Choice, Question, Vote
from django.utils import timezone
from django.contrib import messages
from django.contrib.auth.decorators import login_required


class IndexView(generic.ListView):
    """View for listing the latest published questions that can be voted on."""
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        """Return all published questions which can be voted."""
        question_list = [
            question for question in Question.objects.all()
            if question.is_published() and question.can_vote()]
        return sorted(question_list, key=lambda x: x.pub_date, reverse=True)


class DetailView(generic.DetailView):
    """View for displaying details of a question and allowing users to vote."""
    model = Question
    template_name = 'polls/detail.html'

    def get_queryset(self):
        """Excludes any questions that aren't published yet."""
        return Question.objects.filter(
            pub_date__lte=timezone.now(), end_date__gte=timezone.now())
    
    def get(self, request, pk):
        """GET requests for the detail view of a question."""
        selected_question = get_object_or_404(Question, pk=pk)
        try:
            choice_id = Vote.objects.get(user=request.user,
                                         choice__question=selected_question).choice.id
        except Vote.DoesNotExist:
            choice_id = None
        if not selected_question.can_vote():
            messages.error(request, 'Voting is not allowed.')
            return HttpResponseRedirect(reverse('polls:index'))
        return render(request, 'polls/detail.html',
                      {'question': selected_question, 'choice_id': choice_id})


class ResultsView(generic.DetailView):
    """View for displaying the results of a question."""
    model = Question
    template_name = 'polls/results.html'


@login_required
def vote(request, question_id):
    """Handles the voting for a question's choices."""
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    this_user = request.user
    try:
        # find a vote for this user and this question
        vote = Vote.objects.get(user=this_user, choice__question=question)
        vote.choice = selected_choice
    except Vote.DoesNotExist:
        # no matching vote - create new vote
        vote = Vote(user=this_user, choice=selected_choice)
    vote.save()
    messages.success(request, "Your vote for " + question.question_text
                     + "has been saved.")
    return HttpResponseRedirect(
        reverse('polls:results', args=(question.id,)))
