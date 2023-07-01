from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import ReviewForm
from django.views import View

# from .models import Review


# Create your views here.

class ReviewView(View):
    def get(self, request):
        form = ReviewForm()
        return render(request, "reviews/review.html", {
            "form": form
        })
    
    def post(self, request):
        form = ReviewForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/thank-you")
        return render(request, "reviews/review.html", {
            "form": form
        })




# def review(request):
    # if request.method == "POST":
    #     entered_username = request.POST["username"]
        
    #     if entered_username == "" and len(entered_username) >=100:
    #         return render(request, "reviews/review.html", {
    #             "has_error": True,
    #         })
        
    #     print(entered_username)
    #     return HttpResponseRedirect("/thank-you")
    
    # if request.method == "POST":
    #     form = ReviewForm(request.POST)
    #     if form.is_valid():
            # review = Review(
            #     user_name=form.cleaned_data["user_name"], 
            #     review_text=form.cleaned_data["review_text"], 
            #     rating=form.cleaned_data["rating"]
            #     )
            # review.save()
            # print(form.cleaned_data)
            # form.save()
            # return HttpResponseRedirect("/thank-you")
    # else:
    #     form = ReviewForm()    
    
    # return render(request, "reviews/review.html",{
    #     "form": form,
    # })



def thank_you(request):
    return render(request, "reviews/thank_you.html")