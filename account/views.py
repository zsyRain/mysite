from django.shortcuts import render

# Create your views here.
def user_login(request):
    return render(request, "blog/titles.html", {"blogs": blogs})

