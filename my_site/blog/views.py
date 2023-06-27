# from datetime import date
from django.shortcuts import render, get_object_or_404
from .models import Post, Author, Tag


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
  
  
all_posts = [ 
             
             
             
]

def get_date(post):
  return post['date']



# Create your views here.



def starting_page(request):
  latest_posts = Post.objects.all().order_by("-date")[:3]           
  # sorted_posts = sorted(all_posts, key=get_date)
  # latest_posts = sorted_posts[-3:]
  return render(request, "blog/index.html",{
    "posts":latest_posts
  })
  
def posts(request):
  all_posts = Post.objects.all().order_by("-date")
  return render(request, "blog/all-posts.html",{
    "all_posts":all_posts
  })

def post_details(request,slug):
  # identified_post = next(post for post in all_posts if post['slug'] == slug)
  identified_post = get_object_or_404(Post, slug=slug)
  return render(request, "blog/post-detail.html",{
    "post":identified_post,
    "post_tags":identified_post.tags.all()
  })