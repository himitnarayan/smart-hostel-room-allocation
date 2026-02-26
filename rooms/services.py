from .models import Room, Allocation


# 🔍 Search Logic
def search_rooms(min_capacity=None, has_ac=False, has_washroom=False):
    rooms = Room.objects.all()

    if min_capacity:
        rooms = rooms.filter(capacity__gte=min_capacity)

    if has_ac:
        rooms = rooms.filter(has_ac=True)

    if has_washroom:
        rooms = rooms.filter(has_attached_washroom=True)

    return rooms


# 🎯 Allocation Logic
def allocate_room(students, needs_ac, needs_washroom):

    rooms = Room.objects.filter(
        capacity__gte=students,
        has_ac=needs_ac,
        has_attached_washroom=needs_washroom
    ).order_by('capacity')

    for room in rooms:
        if room.available_seats() >= students:
            room.occupied += students
            room.save()

            Allocation.objects.create(
                room=room,
                students_allocated=students
            )

            return room

    return None