from django.db import models

class Room(models.Model):
    TYPES = [
        ('focus', 'focus'),
        ('team', 'team'),
        ('conference', 'conference')
    ]

    name      = models.CharField(max_length=255)
    tayp      = models.CharField(max_length=10, choices=TYPES)
    capacity  = models.PositiveSmallIntegerField()
    # is_booked = models.BooleanField(default=False)

    def __str__(self) -> str:
        return self.name
    
class Booked(models.Model):
    start_time = models.DateTimeField()
    end_time   = models.DateTimeField()
    room       = models.ForeignKey(Room, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f"{self.start_time}  {self.end_time} - {self.room}"
