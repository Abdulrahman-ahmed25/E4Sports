from django.shortcuts import render
from sportnew.models import SportNew
# Create your views here.
def home_view(request):
    sport_new_list = list(reversed(SportNew.objects.filter(active=True)))

    context = {
        "sport_new_list":sport_new_list,
    }
    return render(request, "home/home.html",context)