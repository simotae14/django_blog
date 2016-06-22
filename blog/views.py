# inserisco pure il 404
from django.shortcuts import render, get_object_or_404
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

# creo la view del dettaglio post
def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    # recuperiamo il post con quell'id
    return render(request, 'blog/post_detail.html', {'post': post})