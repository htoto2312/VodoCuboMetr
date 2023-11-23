from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class MyUser(AbstractUser):
    class Meta:
        db_table = "users"


class Water(models.Model):
    id = models.AutoField(primary_key=True)

    cubometrs = models.IntegerField(max_length=64)
    price_cb = models.IntegerField(max_length=64, default=10)
    is_paid = models.BooleanField(default=False)

    address=models.CharField(max_length=128)
    created_at = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(
        MyUser, db_column="author_id", related_name="notes", on_delete=models.CASCADE
    )

    def __str__(self):
        return self.title

    class Meta:
        db_table = "notes"
