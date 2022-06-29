import uuid
from django.db import models
from django.contrib.auth import get_user_model
from django.core.validators import MinValueValidator, MaxValueValidator

User = get_user_model()


class Store(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    name = models.CharField(max_length=255)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    def get_rating_average(self):
        ratings = Review.objects.filter(store=self)
        if ratings.count() == 0:
            return 0
        return sum(rating.rating for rating in ratings) / ratings.count()


class Adress(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    store = models.ForeignKey(Store, on_delete=models.CASCADE)
    street = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    state = models.CharField(max_length=255)
    zip_code = models.CharField(max_length=255)

    def __str__(self):
        return self.street


class Review(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    store = models.ForeignKey(Store, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.IntegerField(validators=[MinValueValidator(0),
                                             MaxValueValidator(5)])
    comment = models.TextField()

    def __str__(self):
        return self.comment
