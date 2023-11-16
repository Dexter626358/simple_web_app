from django.db import models
from django.contrib.auth.models import User



# Create your models here.

class Product(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    quantity = models.IntegerField()
    added_date = models.DateField(auto_now_add=True)
    image = models.ImageField(upload_to='product_images/')


class CustomUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # Добавьте дополнительные поля, если необходимо

    def __str__(self):
        return self.user.username
