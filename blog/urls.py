from django.conf.urls import url
# importo tutte le views
from . import views

# aggiungiamo il nostro primo modello di URL
urlpatterns = [
    # setto root
    url(r'^$', views.post_list, name='post_list'),
]