from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse



# Create your views here.

def index(request):
    # list_items = ""
    months = list(monthly_challenges.keys())
    
    return render(request,"challenges/index.html", {
        "months":months
    
    })
    
    
    # for month in months:
    #     capitalize_month = month.capitalize()
    #     month_path = reverse("month-challenge", args=[month])
    #     list_items += f"<li><a href=\"{month_path}\">{capitalize_month}</a></li>"

    # # "<li><a href="...">January</a></li><li><a href="...">February</a></li>"

    # response_data = f"<ul>{list_items}</ul>"
    # return HttpResponse(response_data)
    


monthly_challenges = {
    "january": "January",
    "february": "February",
    "march": "March",
    "april": "April",
    "may": "May",
    "june": "June",
    "july": "July",
    "august": "August",
    "september": "September",
    "october": "October",
    "november": "November",
    "december": None,

}


def monthly_challenge_by_number(request, month):
    months = list(monthly_challenges.keys())
    if month > len(months):
        return HttpResponseNotFound("Invalid month")

    redirect_month = months[month - 1]
    redirect_path = reverse("month-challenge", args=[redirect_month])  # /challenge/january
    return HttpResponseRedirect(redirect_path)


def monthly_challenge(request, month):
    try:
        challenge_text = monthly_challenges[month]
        # response_data = f"<h1>{challenge_text}</h1>"
        # response_data = render_to_string("challenges/challenge.html")
        
        return  render(request, "challenges/challenge.html",{
            "text": challenge_text,
            "month_name":month
        })
       
    except:
        return HttpResponseNotFound("<h1>This month is not supported !</h1>")
