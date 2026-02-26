from django import forms
from .models import Room


# Form to Add Room
class RoomForm(forms.ModelForm):
    class Meta:
        model = Room
        fields = [
            'room_no',
            'capacity',
            'has_ac',
            'has_attached_washroom'
        ]


# Search Rooms Form
class SearchForm(forms.Form):
    min_capacity = forms.IntegerField(
        required=False,
        min_value=1,
        label="Minimum Capacity"
    )
    has_ac = forms.BooleanField(
        required=False,
        label="AC Required"
    )
    has_washroom = forms.BooleanField(
        required=False,
        label="Attached Washroom Required"
    )


# Allocation Form (One Student at a Time)
class AllocationForm(forms.Form):
    student_name = forms.CharField(
        max_length=100,
        label="Student Name"
    )

    student_roll_number = forms.CharField(
        max_length=20,
        label="Student Roll Number"
    )

    needs_ac = forms.BooleanField(
        required=False,
        label="AC Required"
    )

    needs_washroom = forms.BooleanField(
        required=False,
        label="Attached Washroom Required"
    )