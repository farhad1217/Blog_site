from django.urls import path
from . import views

urlpatterns = [
    path("", views.landing_page, name="landing_page"),
    path("post", views.all_post_page, name="all_post_page"),
    path("post/<slug:slug>", views.post_detail_page, name="post_detail_page")
]
