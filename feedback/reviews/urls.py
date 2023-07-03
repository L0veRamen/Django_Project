
from django.urls import path
from . import views

urlpatterns = [
    # path("", views.review, name='review'),
    path("", views.ReviewView.as_view(), name='review'),
    # path("thank-you", views.thank_you, name="thank_you"),
    path("thank-you", views.ThankYouView.as_view(), name='thank_you'),
    path("reviews", views.ReviewListView.as_view(), name='reviews_list'),
    path("reviews/favorite", views.AddFavoriteView.as_view(), name='add_favorite'),
    # path("reviews/<int:id>", views.SingleReviewView.as_view(), name='single_review'),
    path("reviews/<int:pk>", views.SingleReviewView.as_view(), name='single_review'),
]

