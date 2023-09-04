from django.db import models

# Create your models here.
class ScrapedData(models.Model):
    url = models.URLField()
    data = models.TextField()

    def __str__(self):
        return self.url