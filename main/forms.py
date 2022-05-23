from django.forms import ModelForm
from .models import Blogs

class BlogForm(ModelForm):
    class Meta:
        model = Blogs
        fields = '__all__'