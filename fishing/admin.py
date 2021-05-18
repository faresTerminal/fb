from django.contrib import admin
from fishing.models import articles, author, Pokes

# Register your models here.
admin.site.register(author)
admin.site.register(articles)
admin.site.register(Pokes)