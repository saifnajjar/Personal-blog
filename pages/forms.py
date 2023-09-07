from django import forms
from .models import Comment

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['name', 'email', 'content']




from django import forms
from .models import ProjectComment

class ProjectCommentForm(forms.ModelForm):
    class Meta:
        model = ProjectComment
        fields = ['name', 'email', 'comment']        



from django import forms
from .models import ContactMessage

class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactMessage
        fields = ['name', 'email', 'subject', 'message']

