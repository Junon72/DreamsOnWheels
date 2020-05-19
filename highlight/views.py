from django.shortcuts import render, redirect, reverse, get_object_or_404, get_list_or_404
from django.contrib.auth.decorators import login_required
from products.models import Original, Vote
from django.contrib.auth.models import User
from django.contrib import messages


def get_highlight(request):
    """Get Originals with highlight status"""

    highlight = get_list_or_404(Original, status='h')
    context = {
        'highlight': highlight,
        'highlight_page': 'active'
    }
    return render(request, "highlight.html", context)

@login_required
def up_vote(request, id):
    if not request.user.is_authenticated:
        messages.danger(request, "You have to login to vote.")
        return redirect('highlight:get_highlight')
    else:
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

