from django.conf.urls import include, url
# importo tutte le views
from . import views

# aggiungiamo il nostro primo modello di URL
urlpatterns = [
    # setto root
    url(r'^$', views.post_list, name='post_list'),
    # setto la vista del dettaglio del post
    url(r'^post/(?P<pk>[0-9]+)/$', views.post_detail, name='post_detail'),
]