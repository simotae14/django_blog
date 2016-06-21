from django.db import models

# Create your models here.
# importo il timezone
from django.utils import timezone

# creo il model Post
class Post(models.Model):
    # creo i campi
    autore = models.ForeignKey('auth.User')
    titolo = models.CharField(max_length = 200)
    testo = models.TextField()
    data_creazione = models.DateTimeField(default=timezone.now)
    data_pubblicazione = models.DateTimeField(blank=True, null=True)

    # metodo pubblica
    def pubblica(self):
        self.data_pubblicazione = timezone.now
        self.save()

    # metodo toString
    def __str__(self):
        return self.titolo