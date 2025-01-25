from django.db import models

# Create your models here.

class Tag(models.Model):
    caption = models.CharField(max_length=20)

    def __str__(self):
        return self.caption
    

class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email_address = models.EmailField(max_length=100)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Post(models.Model):
    title = models.CharField(max_length=100)
    image_name = models.CharField(max_length=100)
    date_posted = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(Author, on_delete=models.SET_NULL, null=True, related_name='posts')
    content = models.TextField()
    slug = models.SlugField(max_length=100, unique=True)
    tags = models.ManyToManyField(Tag, related_name='posts')

    def __str__(self):
        return self.title