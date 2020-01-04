from django.views.generic import ListView, DetailView
from django.http import Http404
from django.urls import reverse
from django_countries import countries
from django.shortcuts import render, redirect
from . import models


class HomeView(ListView):

    """ HomeView Definition """

    model = models.Room
    paginate_by = 10
    paginate_orphans = 5
    ordering = "created"
    context_object_name = "rooms"


class RoomDetail(DetailView):

    """ RoomDetail Definition"""

    model = models.Room


def room_detail(request, pk):
    try:
        room = models.Room.objects.get(pk=pk)
    except models.Room.DoesNotExist:
        raise Http404()
    return render(request, "rooms/detail.html", context={"room": room})


def search(request):
    city = request.GET.get("city", "")
    city = str.capitalize(city)
    room_types = models.RoomType.objects.all()
    return render(
        request,
        "rooms/search.html",
        context={"city": city, "countries": countries, "room_types": room_types},
    )
