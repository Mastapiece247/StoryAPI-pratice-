from django.db import models

# Create your models here.


class Novel(models.Model):
    title = models.CharField(max_length=50)
    author = models.CharField(max_length=60)
    published_date = models.DateTimeField()
    isbn = models.CharField(max_length=13)

    def __str__(self):
        return self.title
