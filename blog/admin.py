from django.contrib import admin
from .models import Post, Author, Tag

# Register your models here.

class PostAdmin(admin.ModelAdmin):
    list_filter = ("author", "tags", "date_posted")
    list_display = ("title", "date_posted", "author")
    prepopulated_fields = {'slug': ('title',)}


admin.site.register(Author)
admin.site.register(Tag)
admin.site.register(Post, PostAdmin)
