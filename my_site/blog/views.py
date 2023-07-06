# from datetime import date
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import Post, Author, Tag
from .forms import CommentForm
from django.views.generic import ListView, DetailView
from django.views import View


# all_posts = [
#   {
#     "slug":"hike-in-the-mountains",
#   "image":"mountain.jpg",
#   "author":"Chen",
#   "date":date(2023,6,12),
#   "title":"Mountain Hiking",
#   "excerpt":"There's nothing like the views you get when hiking in the mountains! And I wasn't even prepared for this trip!",
#   "content":"""LOL1"""},
#   {
#     "slug":"nature-at-its-best",
#   "image":"maples.jpg",
#   "author":"Chen",
#   "date":date(2023,6,11),
#   "title":"Nature At Its Best",
#   "excerpt":"Nature is amazing! The color of these leaves is just perfect.",
#   "content":"""LOL2"""
#   },
#   {
#     "slug":"programming-is-fun",
#   "image":"coding.png",
#   "author":"Chen",
#   "date":date(2023,6,10),
#   "title":"Programming Is Fun",
#   "excerpt":"Who would've thought that programming is so much fun!",
#   "content":"""LOL2"""
#   },

# Create your views here.

class StartingPageView(ListView):
    template_name = "blog/index.html"
    model = Post
    ordering = ["-date"]
    context_object_name = "posts"

    def get_queryset(self):
        queryset = super().get_queryset()
        data = queryset[:3]
        return data


class AllPostsView(ListView):
    template_name = "blog/all-posts.html"
    model = Post
    ordering = ["-date"]
    context_object_name = "all_posts"


class SinglePostView(View):
    def is_stored_post(self, request, post_id):
        stored_posts = request.session.get("stored_posts")
        if stored_posts is not None:
          is_saved_for_later = post_id in stored_posts
        else:
          is_saved_for_later = False

        return is_saved_for_later

    def get(self, request, slug):
        post = Post.objects.get(slug=slug)
        
        context = {
            "post": post,
            "post_tags": post.tags.all(),
            "comment_form": CommentForm(),
            "comments": post.comments.all().order_by("-id"),
            "saved_for_later": self.is_stored_post(request, post.id)
        }
        return render(request, "blog/post-detail.html", context)

    def post(self, request, slug):
        comment_form = CommentForm(request.POST)
        post = Post.objects.get(slug=slug)

        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.save()

            return HttpResponseRedirect(reverse("post-detail-page", args=[slug]))

        context = {
            "post": post,
            "post_tags": post.tags.all(),
            "comment_form": comment_form,
            "comments": post.comments.all().order_by("-id"),
            "saved_for_later": self.is_stored_post(request, post.id)
        }
        return render(request, "blog/post-detail.html", context)


class ReadLaterView(View):
    def get(self, request):
        stored_posts = request.session.get("stored_posts")

        context = {}

        if stored_posts is None or len(stored_posts) == 0:
            context["posts"] = []
            context["has_posts"] = False
        else:
          posts = Post.objects.filter(id__in=stored_posts)
          context["posts"] = posts
          context["has_posts"] = True

        return render(request, "blog/stored-posts.html", context)


    def post(self, request):
        stored_posts = request.session.get("stored_posts")

        if stored_posts is None:
          stored_posts = []

        post_id = int(request.POST["post_id"])

        if post_id not in stored_posts:
          stored_posts.append(post_id)
        else:
          stored_posts.remove(post_id)

        request.session["stored_posts"] = stored_posts
        
        return HttpResponseRedirect("/")


# class SinglePostView(DetailView):
#   template_name = "blog/post-detail.html"
#   model = Post

#   def get_context_data(self, **kwargs):
#       context = super().get_context_data(**kwargs)
#       context["post_tags"] = self.object.tags.all()
#       context["comment_form"] = CommentForm()
#       return context


# def starting_page(request):
#   latest_posts = Post.objects.all().order_by("-date")[:3]
#   # sorted_posts = sorted(all_posts, key=get_date)
#   # latest_posts = sorted_posts[-3:]
#   return render(request, "blog/index.html",{
#     "posts":latest_posts
#   })

# def posts(request):
#   all_posts = Post.objects.all().order_by("-date")
#   return render(request, "blog/all-posts.html",{
#     "all_posts":all_posts
#   })

# def post_details(request,slug):
#   # identified_post = next(post for post in all_posts if post['slug'] == slug)
#   identified_post = get_object_or_404(Post, slug=slug)
#   return render(request, "blog/post-detail.html",{
#     "post":identified_post,
#     "post_tags":identified_post.tags.all()
#   })
