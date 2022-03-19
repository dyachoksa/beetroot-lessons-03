from django.urls import path

from .views import GalleryListView, GalleryDetailView

app_name = 'galleries'

urlpatterns = [
    path('<int:pk>/', GalleryDetailView.as_view(), name='detail'),
    path('', GalleryListView.as_view(), name='list'),
]
