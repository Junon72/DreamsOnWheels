from django.shortcuts import render
from products.models import Original

def get_highlight(request):
    """Get Originals with highlight status"""
    
    highlight = Original.objects.filter(status='h')
    context = {
        'highlight': highlight,
        'highlight_page': 'active'
    }
    return render(request, "highlight.html", context)
