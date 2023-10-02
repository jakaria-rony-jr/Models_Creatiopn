from django.db import models

# Create your models here.

class Profile(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='pros')
    description = models.CharField(max_length=500)

    class Meta:
        verbose_name_plural = ("Profile")

    def __str__(self):
        return self.name