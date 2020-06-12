from django.shortcuts import render, redirect, reverse, get_object_or_404, get_list_or_404
from django.contrib.auth.decorators import login_required
from products.models import Original, Vote
from django.contrib.auth.models import User
from django.contrib import messages


def get_highlight(request):
    """
    Get Originals objects with highlight status and
    render them.
    """

    highlight = get_list_or_404(Original, status='h')
    context = {
        'highlight': highlight,
        'highlight_page': 'active',
        'title': 'Highlights'
    }
    return render(request, "highlight.html", context)

# @login_required
def up_vote(request, id):
    """
    Check if the user is logged in, and prevent user not
    not logged in from voting.
    Get the Original objects associated with the vote function
    and add a vote if the user has not voted for this
    specific entry yet.
    """
    if not request.user.is_authenticated:
        messages.warning(request, "You have to login to vote.")
        return redirect('highlight:get_highlight')
    else:
        # Processing post requests
        if request.method == 'POST':
            highlight = get_object_or_404(Original, id=id)
            vote, created = Vote.objects.get_or_create(highlight=highlight, user=request.user)
            if created:
                highlight.votes += 1
                highlight.save()
                messages.success(request, "Thank you. Your vote has been accounted!")
            else:
                messages.info(request, "You have already voted for this highlight")
            return redirect('highlight:get_highlight')

