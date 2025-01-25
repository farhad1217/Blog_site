from django.shortcuts import render, get_list_or_404
from .models import Post

# Create your views here.


def landing_page(request):
    latest_post = Post.objects.all().order_by("-date_posted")[:3]
    return render(request, "blog/landing_page.html", {
        "latest_post" : latest_post,
    })

def all_post_page(request):
    return render(request, "blog/all_post.html", {
        "all_post" : Post.objects.all()
    })

def post_detail_page(request, slug):
    try:
        single_post = Post.objects.get(slug=slug)
    except:
        return render(request, "blog/404.html")
    return render(request, "blog/post_detail.html", {
        "post" : single_post,
        "tags" : single_post.tags.all()
    })


