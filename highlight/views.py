from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib.auth.decorators import login_required
from products.models import Original
from django.contrib.auth.models import User


def get_highlight(request):
    """Get Originals with highlight status"""
    
    highlight = Original.objects.filter(status='h')
    context = {
        'highlight': highlight,
        'highlight_page': 'active'
    }
    return render(request, "highlight.html", context)

