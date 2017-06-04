from django.db import models


class ElectionCandidate(models.Model):
    name = models.CharField(max_length=255)
    image_url = models.CharField(blank=True, max_length=255)

    twitter_username = models.CharField(blank=True, max_length=255)
    facebook_page_url = models.CharField(blank=True, max_length=255)
