from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from django.contrib import messages
from django.http import HttpResponseForbidden
from django.urls import reverse_lazy
from django.contrib.auth.models import User
from .models import Post, Comment
from .forms import CommentForm, UpdateCommentForm
from bootstrap_modal_forms.generic import BSModalUpdateView, BSModalDeleteView


def get_posts(request):
    """
    Create a view that will return a list
    of posts that were published prior to 'now'
    and render them to the 'blogposts.html
    """
    post_list = Post.objects.filter(
        published_date__lte=timezone.now()).order_by('-published_date')
    paginator = Paginator(post_list, 6)

    page = request.GET.get('page')
    posts = paginator.get_page(page)
    context = {
        'posts': posts,
        'blogs_page': 'active',
        'title': 'BLogs'
        }
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
    users = User.objects.all().select_related('profiles')
    comment = None
    # Processing post requests
    if request.method == 'POST':
        if not request.user.is_authenticated:
            return redirect('accounts:login')
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            comment = comment_form.cleaned_data['content']
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.owner = request.user
            comment.save()
            messages.success(
                request,
                "Thank you for commenting! Your comment is being reviewed"
            )
            return redirect('posts:post_detail', pk=post.pk)
    else:
        comment_form = CommentForm()

    context = {
        'comments': comments,
        'users': users,
        'comment_form': comment_form,
        'post': post,
        'title': 'Blog'
    }

    return render(request, "postdetail.html", context)


class CommentUpdateView(BSModalUpdateView):
    """
    Update comment using django-bootstrap-modal-forms package.
    The form_valid method is overdriven to get the correct success_url.
    Instance call is used to get the parent post id for the url path,
    returning to the the postdetail page after update.
    """

    model = Comment
    template_name = 'edit_comment.html'
    form_class = UpdateCommentForm

    def form_valid(self, form):
        instance = form.cleaned_data['content']
        instance = form.save()
        self.success_url = reverse_lazy(
            'posts:post_detail',
            kwargs={'pk': instance.post.id}
        )
        return super(CommentUpdateView, self).form_valid(form)


class CommentDeleteView(BSModalDeleteView):
    """
    Delete comment using django-bootstrap-modal-forms package.
    The get_success_url method is used to get the correct path back
    back to the postdetail page after delete. The method calls related
    post object to get the correct parent post id.
    """

    model = Comment
    template_name = 'delete_comment.html'
    success_message = 'Success! Comment was delete.'

    def get_success_url(self):
        post = self.object.post
        post_id = self.object.post.id
        return reverse_lazy('posts:post_detail', kwargs={'pk': post.id})
