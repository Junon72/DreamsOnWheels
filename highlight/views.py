from django.shortcuts import (
    get_list_or_404,
    get_object_or_404,
    render,
    redirect
)
from products.models import Original, Vote
from django.contrib import messages


def get_highlight(request):
    """
    Get Originals objects with highlight status and
    render them.
    """

    highlight = Original.objects.filter(status='h')
    context = {
        'highlight': highlight,
        'highlight_page': 'active',
        'title': 'Highlights'
    }
    return render(request, "highlight.html", context)


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
        if request.method == 'POST':
            highlight = get_object_or_404(Original, id=id)
            vote, created = Vote.objects.get_or_create(
                highlight=highlight,
                user=request.user
            )
            if created:
                highlight.votes += 1
                highlight.save()
                messages.success(
                    request,
                    "Thank you. Your vote has been accounted!"
                )
            else:
                messages.info(
                    request,
                    "You have already voted for this highlight"
                )
            return redirect('highlight:get_highlight')
