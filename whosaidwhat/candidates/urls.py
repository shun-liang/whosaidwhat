from django.conf.urls import url

from . import views

urlpatterns = [
    url(
        regex=r'^$',
        view=views.ElectionCandidateListView.as_view(),
        name='list'
    ),
    url(
        regex=r'^(?P<pk>[\w.@+-]+)/$',
        view=views.ElectionCandidateDetailView.as_view(),
        name='detail'
    ),
]
