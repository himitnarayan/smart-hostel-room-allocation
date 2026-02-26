from django.shortcuts import render, redirect, get_object_or_404
from .models import Room
from .forms import RoomForm, SearchForm, AllocationForm
from .services import search_rooms, allocate_room


# 🏠 HOME - View All Rooms
def room_list(request):
    rooms = Room.objects.all()
    return render(request, 'room_list.html', {'rooms': rooms})


# ➕ Add Room
def add_room(request):
    form = RoomForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('room_list')

    return render(request, 'add_room.html', {'form': form})


# 🔍 Search Rooms
def search_room_view(request):
    form = SearchForm(request.GET or None)
    rooms = Room.objects.all()

    if form.is_valid():
        min_capacity = form.cleaned_data.get('min_capacity')
        has_ac = form.cleaned_data.get('has_ac')
        has_washroom = form.cleaned_data.get('has_washroom')

        rooms = search_rooms(min_capacity, has_ac, has_washroom)

    return render(request, 'search_room.html', {
        'form': form,
        'rooms': rooms
    })


# 🎯 Allocate Student
def allocate_room_view(request):
    form = AllocationForm(request.POST or None)
    allocated_room = None
    message = None

    if request.method == "POST" and form.is_valid():
        student_name = form.cleaned_data['student_name']
        student_roll_number = form.cleaned_data['student_roll_number']
        needs_ac = form.cleaned_data['needs_ac']
        needs_washroom = form.cleaned_data['needs_washroom']

        allocated_room = allocate_room(
            student_name,
            student_roll_number,
            needs_ac,
            needs_washroom
        )

        if not allocated_room:
            message = "Room not available"

    return render(request, 'allocate_room.html', {
        'form': form,
        'allocated_room': allocated_room,
        'message': message
    })


# 🏨 Room Detail (See Students Inside)
def room_detail(request, room_id):
    room = get_object_or_404(Room, id=room_id)
    students = room.students.all()

    return render(request, 'room_detail.html', {
        'room': room,
        'students': students
    })