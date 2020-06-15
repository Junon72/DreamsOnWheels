from django import forms
from .models import Comment
from bootstrap_modal_forms.forms import BSModalForm


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        widgets = {
            'content': forms.Textarea(attrs={'rows': 4}),
        }
        fields = ['content']
        labels = {
            'content': 'Comment:',
        }


class UpdateCommentForm(BSModalForm):
    class Meta:
        model = Comment
        widgets = {
            'content': forms.Textarea(attrs={'rows': 8})
        }
        fields = ['content']
