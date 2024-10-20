from django.db import models

class VegetablePrice(models.Model):
    name = models.CharField(max_length=100)
    min_price = models.CharField(max_length=100)
    max_price = models.CharField(max_length=100)
    avg_price = models.CharField(max_length=100)
    date = models.DateField(auto_now_add=True)

    def __str__(self):
            return f"{self.name} - Min: {self.min_price}, Max: {self.max_price}, Avg: {self.avg_price} (on {self.date})"
