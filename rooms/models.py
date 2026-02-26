from django.db import models


class Room(models.Model):
    room_no = models.CharField(max_length=10, unique=True)
    capacity = models.PositiveIntegerField()
    has_ac = models.BooleanField(default=False)
    has_attached_washroom = models.BooleanField(default=False)
    occupied = models.PositiveIntegerField(default=0)  # NEW FIELD
    created_at = models.DateTimeField(auto_now_add=True)

    def available_seats(self):
        return self.capacity - self.occupied

    def __str__(self):
        return f"Room {self.room_no}"


# NEW TABLE
class Allocation(models.Model):
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    students_allocated = models.PositiveIntegerField()
    allocated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.students_allocated} students → Room {self.room.room_no}"