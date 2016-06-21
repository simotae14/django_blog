from django.shortcuts import render
# aggiungo anche il timezone
from django.utils import timezone

# importo il model Post
from .models import Post

# Create your views here.
# definisco la view che lega la richiesta con un template
def post_list(request):
    # recupero l'elenco di post pubblicati entro ora e ordinati per data pubblicazione
    posts = Post.objects.filter(data_pubblicazione__lte=timezone.now()).order_by('data_pubblicazione')
    return render(request, 'blog/post_list.html', {'posts': posts})