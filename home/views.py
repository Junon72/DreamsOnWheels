from django.shortcuts import render


def index(request):
    """Return the index.html file"""
    context = {"index_page": "active"}
    return render(request, "index.html", context)