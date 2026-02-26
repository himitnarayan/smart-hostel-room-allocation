from .models import Room, Allocation


def search_rooms(min_capacity=None, has_ac=False, has_washroom=False):
    rooms = Room.objects.all()

    if min_capacity:
        rooms = rooms.filter(capacity__gte=min_capacity)

    if has_ac:
        rooms = rooms.filter(has_ac=True)

    if has_washroom:
        rooms = rooms.filter(has_attached_washroom=True)

    return rooms


def allocate_room(student_name, student_roll_number, needs_ac, needs_washroom):

    # Get rooms matching requirements
    rooms = Room.objects.filter(
        has_ac=needs_ac,
        has_attached_washroom=needs_washroom
    ).order_by('capacity')

    for room in rooms:
        # Check if room has available seat
        if room.available_seats() > 0:

            # Update occupied count
            room.occupied += 1
            room.save()

            # Create allocation record
            Allocation.objects.create(
                room=room,
                student_name=student_name,
                student_roll_number=student_roll_number
            )

            return room

    # If no room available
    return None