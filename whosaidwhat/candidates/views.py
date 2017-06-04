from django.views.generic import DetailView, ListView

from .models import ElectionCandidate


class ElectionCandidateDetailView(DetailView):
    model = ElectionCandidate


class ElectionCandidateListView(ListView):
    model = ElectionCandidate
