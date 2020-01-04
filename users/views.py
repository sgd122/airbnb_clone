from django.shortcuts import render

# Create your views here.
def user_detail(request, pk):

    return render(request, "users/detail.html")
