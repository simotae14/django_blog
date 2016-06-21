from django.shortcuts import render

# Create your views here.
# definisco la view che lega la richiesta con un template
def post_list(request):
    return render(request, 'blog/post_list.html', {})