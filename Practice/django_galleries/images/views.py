from django.views.generic import ListView, DetailView

from .models import Gallery


class GalleryListView(ListView):
    model = Gallery
    queryset = Gallery.objects.select_related('user').order_by('-created_at')
    context_object_name = "galleries"
    template_name = "galleries/list.html"


class GalleryDetailView(DetailView):
    model = Gallery
    context_object_name = "gallery"
    template_name = "galleries/detail.html"
