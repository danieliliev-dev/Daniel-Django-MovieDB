from django.db import models

class Movie(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    release_date = models.DateField()
    director = models.CharField(max_length=255)
    genre = models.CharField(max_length=100)
    user_rating = models.FloatField(default=0.0)
    is_favorite = models.BooleanField(default=False)
    cover_image = models.ImageField(upload_to='movies/covers/', null=True, blank=True)

    def __str__(self):
        return self.title