import datetime as dt
import uuid
import os.path

from django.conf import settings
from django.db import models
from django.urls import reverse
from imagekit.models import ImageSpecField
from pilkit.processors import SmartResize


def upload_image_to(instance, filename):
    _, ext = os.path.splitext(filename)

    filename = f"{uuid.uuid4()}{ext}"

    return os.path.join('images', dt.date.today().strftime('%Y/%m'), filename)


class Gallery(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='galleries', db_index=True
    )
    name = models.CharField(max_length=150)
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('-created_at',)
        verbose_name = 'gallery'
        verbose_name_plural = 'galleries'

    def __str__(self):
        return self.name

    def __repr__(self):
        return "<Gallery id={} user={} name={}>".format(self.pk, self.user_id, self.name)

    @property
    def main_image(self):
        return self.images.first()

    def get_absolute_url(self):
        return reverse('galleries:detail', kwargs={"pk": self.pk})


class GalleryImage(models.Model):
    gallery = models.ForeignKey(Gallery, on_delete=models.CASCADE, related_name='images', db_index=True)
    image = models.ImageField(max_length=300, upload_to=upload_image_to)
    title = models.CharField(max_length=100, blank=True, null=True)
    position = models.SmallIntegerField(blank=True, default=1)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    image_preview = ImageSpecField(
        source="image", processors=[SmartResize(600, 400)], format='JPEG', options={'quality': 90}
    )

    class Meta:
        ordering = ['position']
        verbose_name = 'gallery image'
        verbose_name_plural = 'gallery images'

    def __str__(self):
        return self.image.name

    def __repr__(self):
        return "<GalleryImage id={} gallery={} image={}>".format(
            self.pk, self.gallery_id, self.image.name
        )
