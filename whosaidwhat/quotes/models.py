from django.db import models

from whosaidwhat.candidates.models import ElectionCandidate
from whosaidwhat.users.models import User


class QuoteQuestion(models.Model):
    asked_by = models.ForeignKey(to=User)
    created_at = models.DateTimeField(auto_now=True)

    source = models.ForeignKey(to=ElectionCandidate)
    quote = models.TextField()
    quote_date = models.DateField(null=True, blank=True)
    quote_location = models.CharField(blank=True, max_length=255)

    @property
    def title(self):
        title_text = f'Did {self.source.name} say that {self.quote}'
        if self.quote_location:
            title_text = f'{title_text} at quote_location'
        if self.quote_date:
            title_text = f'{title_text} on quote_date'
        return f'{title_text}?'


class QuoteAnswer(models.Model):
    question = models.ForeignKey(to=QuoteQuestion)
    author = models.ForeignKey(to=User)
    accuracy_choices = (
        ('0', 'No'),
        ('1', 'Yes'),
        ('2', 'Inaccurate/Out-of-context'),
    )
    accuracy = models.CharField(max_length=1, choices=accuracy_choices)
    created_at = models.DateTimeField()
    content = models.TextField()


class VoteOnQuestion(models.Model):
    voted_to = models.ForeignKey(to=QuoteQuestion)
    voted_by = models.ForeignKey(to=User)
    created_at = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = ('voted_to', 'voted_by')


class VoteOnAnswer(models.Model):
    voted_to = models.ForeignKey(to=QuoteAnswer)
    voted_by = models.ForeignKey(to=User)
    created_at = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = ('voted_to', 'voted_by')
