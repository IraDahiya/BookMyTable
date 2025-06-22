from django.db import models

class Reservation(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    date = models.DateField()
    time = models.TimeField()
    guests = models.IntegerField()

    def __str__(self):
        return f"{self.name} - {self.date} at {self.time}"
