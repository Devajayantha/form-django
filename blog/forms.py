from django.forms import ModelForm, HiddenInput
from blog.models import *


class CommentForm(ModelForm):
    class Meta:
        model = Comment
        # file inputan yang terdapat pada menu form
        fields =['content','post']
        # digunakna untuk menghide inputan pada form
        widgets = {'post': HiddenInput()}

class UploadForm(ModelForm):
    class Meta:
        model = Upload
        fields = ['title_pic','model_pic']
        # picture =['model_pic']]

