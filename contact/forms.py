from django import forms
from .models import Contact


# class ContactForm(forms.Form):
#     name = forms.CharField(required=True)
#     from_email = forms.EmailField(required=True)
#     subject = forms.CharField(required=True)
#     message = forms.CharField(required=True, widget=forms.Textarea)

#     def __init__(self, *args, **kwargs):
#         super(ContactForm, self).__init__(*args, **kwargs)
#         self.fields['name'].label = "Your name:"
#         self.fields['from_email'].label = "Your email:"
#         self.fields['message'].label = "Your message:"

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        exclude = ['date']
        widgets = {
            'message': forms.Textarea(attrs={'rows': 8})
        }
        fields = ['name', 'from_email', 'subject', 'message']
        labels = {
            'message': 'Message:',
        }