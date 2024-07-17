from django.db import models


# lets us explicitly set upload path and filename
from user_auth.models import User


def upload_to(instance, filename):
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    return "user_{0}/{1}".format(instance.author.id, filename)


class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return f'{self.name} - {self.id}'


class Photo(models.Model):
    descriptions = models.TextField(default='', blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="photos")
    image_url = models.ImageField(upload_to=upload_to, unique=True)
    average_rating = models.FloatField(
        default=0,
        # editable=False
    )
    tags = models.ManyToManyField(Tag, blank=True)


class Comment(models.Model):
    photo = models.ForeignKey(Photo, on_delete=models.CASCADE)
    text = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class PhotoRating(models.Model):

    class Stars(models.IntegerChoices):
        WORST = 1
        BAD = 2
        NEUTRAL = 3
        GOOD = 4
        EXCELLENT = 5

    amount_stars = models.IntegerField(choices=Stars.choices)
    photo = models.ForeignKey(Photo, on_delete=models.CASCADE, related_name="photo_ratings")
    valuer = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('photo', 'valuer')

