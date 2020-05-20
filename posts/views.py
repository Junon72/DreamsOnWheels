from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Post, Comment
from .forms import CommentForm

def get_posts(request):
    """
    Create a view that will return a list 
    of posts that were published prior to 'now'
    and render them to the 'blogposts.html
    """
    posts = Post.objects.filter(published_date__lte=timezone.now()
        ).order_by('-published_date')

    context = {
        'posts': posts,
        'blogs_page': 'active'}
    return render(request, "blogposts.html", context)


def post_detail(request, pk):
    """
    Create a view that will return a selected
    post and associated comments and a comment
    from for user to leave comments
    """
    post = get_object_or_404(Post, pk=pk)
    post.views += 1
    post.save()
    comments = Comment.objects.order_by('-created_date')
    comment = None
    # Processing post requests
    if request.method == 'POST':
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.owner = request.user
            comment.save()
            return redirect('post_detail', pk=post.pk)
    else:
        comment_form = CommentForm()

    context = {
        'comments': comments,
        'comment_form': comment_form,
        'post': post
    }

    return render(request, "postdetail.html", context)
