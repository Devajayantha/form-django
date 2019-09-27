from django.forms import ModelForm, HiddenInput
from blog.models import Comment


class CommentForm(ModelForm):
    class Meta:
        model = Comment
        # file inputan yang terdapat pada menu form
        fields =['content','post']
        # digunakna untuk menghide inputan pada form
        widgets = {'post': HiddenInput()}


