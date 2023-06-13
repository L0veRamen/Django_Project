from datetime import date
from django.shortcuts import render

all_posts = [
  {
    "slug":"hike-in-the-mountains",
  "image":"mountain.jpg",
  "author":"Chen",
  "date":date(2023,6,12),
  "title":"Mountain Hiking",
  "excerpt":"There's nothing like the views you get when hiking in the mountains! And I wasn't even prepared for this trip!",
  "content":"""LOL1"""},
  {
    "slug":"maples-are-beautiful",
  "image":"maples.jpg",
  "author":"Chen",
  "date":date(2023,6,11),
  "title":"Nature At Its Best",
  "excerpt":"Nature is amazing! The color of these leaves is just perfect.",
  "content":"""LOL2"""
  },
  {
    "slug":"programming-is-fun",
  "image":"coding.png",
  "author":"Chen",
  "date":date(2023,6,10),
  "title":"Programming Is Fun",
  "excerpt":"Who would've thought that programming is so much fun!",
  "content":"""LOL2""" 
  },
  
  
]

def get_date(post):
  return post['date']



# Create your views here.



def starting_page(request):
  sorted_posts = sorted(all_posts, key=get_date)
  latest_posts = sorted_posts[-3:]
  return render(request, "blog/index.html",{
    "posts":latest_posts
  })
  
def posts(request):
  return render(request, "blog/all-posts.html",{
    "all_posts":all_posts
  })

def post_details(request,slug):
  identified_post = next(post for post in all_posts if post['slug'] == slug)
  return render(request, "blog/post-detail.html",{
    "post":identified_post
  })