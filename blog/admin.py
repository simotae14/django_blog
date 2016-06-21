from django.contrib import admin

from .models import Post

# Register your models here.
# inserisco i modelli su cui fare operazioni CRUD
admin.site.register(Post)