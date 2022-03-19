from django.contrib import admin

from .models import Gallery, GalleryImage


@admin.register(GalleryImage)
class GalleryImageAdmin(admin.ModelAdmin):
    date_hierarchy = "created_at"

    search_fields = ("title",)

    list_display = ("__str__", "gallery", "position", "title", "created_at")
    list_filter = ("created_at",)
    list_select_related = ("gallery",)


class InlineGalleryImage(admin.StackedInline):
    model = GalleryImage
    extra = 1
    max_num = 10


@admin.register(Gallery)
class GalleryAdmin(admin.ModelAdmin):
    date_hierarchy = "created_at"

    search_fields = ("name",)

    list_display = ("name", "user", "created_at")
    list_filter = ("created_at",)
    list_select_related = ("user",)

    inlines = [
        InlineGalleryImage,
    ]
