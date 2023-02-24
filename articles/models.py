from django.db import models
from django.conf import settings
from django.urls import reverse


class Article(models.Model):
    title = models.CharField(max_length=254)
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )

    def get_absolute_url(self):
        return reverse("article_detail", kwargs={"pk": self.pk})

    def __str__(self):
        return self.title
