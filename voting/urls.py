from django.urls import path, include
from .views import (
    HomePageView,
    CandidateListView,
    VotingView,
    ResultView,
    VotingClosedView,
    VotingFailureView,
    AlreadyVotedView,
    VotingSuccessView,
)

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('candidate-list/', CandidateListView.as_view(), name='candidate_list'),
    path('vote/', VotingView.as_view(), name='vote'),
    path('result/', ResultView.as_view(), name='result'),
    path('voting-closed/', VotingClosedView.as_view(), name='voting_closed'),
    path('voting-failure/', VotingFailureView.as_view(), name='voting_failure'),
    path('already-voted/', AlreadyVotedView.as_view(), name='already_voted'),
    path('voting-success/', VotingSuccessView.as_view(), name='voting_success'),
    path('accounts/', include('allauth.urls')),
]
