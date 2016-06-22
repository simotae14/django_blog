# inserisco pure il 404
from django.shortcuts import render, get_object_or_404
# aggiungo anche il timezone
from django.utils import timezone

# importo il model Post
from .models import Post

from .forms import PostForm

# importo la redirezione per instradare a seguito del salvataggio di un post al suo dettaglio
from django.shortcuts import redirect

# Create your views here.
# definisco la view che lega la richiesta con un template
def post_list(request):
    # recupero l'elenco di post pubblicati entro ora e ordinati per data pubblicazione
    posts = Post.objects.filter(data_pubblicazione__lte=timezone.now()).order_by('-data_pubblicazione')
    return render(request, 'blog/post_list.html', {'posts': posts})

# creo la view del dettaglio post
def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    # recuperiamo il post con quell'id
    return render(request, 'blog/post_detail.html', {'post': post})


# aggiungo la view della creazione di un nuovo post
# ho due casi, il primo accesso alla pagina in cui il form è vuoto
# il secondo in cui invio il form compilato
def post_new(request):
    # se il form è compilato
    if request.method == "POST":
        # creo il nostro PostForm con i dati insetiti dall'utente
        form = PostForm(request.POST)
        # controlliamo che il form passato sia corretto
        if form.is_valid():
            # con il parametro commit=False non vogliamo salvare il form
            # perché prima vogliamo salvare anche autore
            post = form.save(commit=False)
            post.autore = request.user
            post.data_pubblicazione = timezone.now()
            # ora salvo
            post.save()
            # redirigo al dettaglio
            return redirect('blog.views.post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'blog/post_edit.html', {'form': form})

# aggiungo la view per il post_edit, passo il pk attraverso l'url
def post_edit(request, pk):
    # recupero il post oppure pagina vuota
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        # instance significa che quando creeremo il form gli passo come instance anche post
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.autore = request.user
            post.data_pubblicazione = timezone.now()
            post.save()
            return redirect('blog.views.post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_edit.html', {'form': form})