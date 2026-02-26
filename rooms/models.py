from django.db import models


class Room(models.Model):
    room_no = models.CharField(max_length=10, unique=True)
    capacity = models.PositiveIntegerField()
    has_ac = models.BooleanField(default=False)
    has_attached_washroom = models.BooleanField(default=False)
    occupied = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    def available_seats(self):
        return self.capacity - self.occupied

    def is_full(self):
        return self.occupied >= self.capacity

    def __str__(self):
        return f"Room {self.room_no}"


class Allocation(models.Model):
    room = models.ForeignKey(
        Room,
        on_delete=models.CASCADE,
        related_name="students"
    )
    student_name = models.CharField(max_length=100)
    student_roll_number = models.CharField(max_length=20)
    allocated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.student_name} ({self.student_roll_number}) - Room {self.room.room_no}"