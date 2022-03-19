from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from images.models import Gallery


def index(request):
    latest_galleries = Gallery.objects.select_related("user").order_by("-created_at")[:3]

    context = {
        "latest_galleries": latest_galleries,
    }

    return render(request, "pages/index.html", context=context)


@login_required
def profile(request):
    return render(request, "pages/profile.html")
