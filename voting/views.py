from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import TemplateView
from .models import Candidate, VotingPosition, Vote
from datetime import datetime

class HomePageView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'home.html')

class CandidateListView(View):
    def get(self, request, *args, **kwargs):
        positions = VotingPosition.objects.filter(start_date__lte=datetime.now(), end_date__gte=datetime.now())
        candidates = Candidate.objects.filter(position__in=positions)
        context = {'candidates': candidates}
        return render(request, 'candidate_list.html', context)


class VotingView(TemplateView):
    template_name = 'vote.html'

    def get(self, request, *args, **kwargs):
        current_time = datetime.now().time()
        if current_time < datetime.strptime('08:00:00', '%H:%M:%S').time() or current_time > datetime.strptime('18:00:00', '%H:%M:%S').time():
            return redirect('voting_closed')

        active_positions = VotingPosition.objects.filter(start_date__lte=datetime.now(), end_date__gte=datetime.now())

        # Get the user's already voted position IDs from session
        user_voted_positions = request.session.get('user_voted_positions', [])

        return render(request, self.template_name, {'active_positions': active_positions, 'user_voted_positions': user_voted_positions})

    def post(self, request, *args, **kwargs):
        current_time = datetime.now().time()
        if current_time < datetime.strptime('08:00:00', '%H:%M:%S').time() or current_time > datetime.strptime('18:00:00', '%H:%M:%S').time():
            return redirect('voting_closed')

        active_positions = VotingPosition.objects.filter(start_date__lte=datetime.now(), end_date__gte=datetime.now())

        # Get the user's already voted position IDs from session
        user_voted_positions = request.session.get('user_voted_positions', [])

        for position in active_positions:
            candidate_id = request.POST.get(f'candidate_{position.id}')

            # Check if the user has already voted for this position
            if position.id in user_voted_positions:
                continue

            # If candidate ID is found in the form submission, create a vote
            if candidate_id:
                candidate = Candidate.objects.get(id=candidate_id)
                Vote.objects.create(candidate=candidate, user=request.user)

                # Mark the position as voted in the user's session
                user_voted_positions.append(position.id)

        # Save the updated user's voted position IDs in the session
        request.session['user_voted_positions'] = user_voted_positions

        # Check if the user has voted for all positions
        all_positions_voted = all(position.id in user_voted_positions for position in active_positions)

        if all_positions_voted:
            # If the user has voted for all positions, redirect to the "Voting Success" page
            return redirect('voting_success')
        else:
            # If the user has not voted for all positions, redirect to the "Already Voted" page
            return redirect('already_voted')
    

class ResultView(View):
    def get(self, request, *args, **kwargs):
        candidates = Candidate.objects.all()
        results = []
        total_votes = Vote.objects.count()
        for candidate in candidates:
            votes = Vote.objects.filter(candidate=candidate).count()
            percentage = votes / total_votes * 100 if total_votes > 0 else 0
            results.append({'candidate': candidate, 'votes': votes, 'percentage': percentage})
        context = {'results': results}
        return render(request, 'result.html', context)

class VotingClosedView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'voting_closed.html')

class VotingFailureView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'voting_failure.html')

class AlreadyVotedView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'already_voted.html')

class VotingSuccessView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'voting_success.html')
