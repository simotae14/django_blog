from django import forms

from .models import Post

class PostForm(forms.ModelForm):
    # dice a django che model usare per questo form
    class Meta:
        model = Post
        # autore omesso perché è la persona connessa e data creazione si genera da sola
        fields = ('titolo', 'testo',)