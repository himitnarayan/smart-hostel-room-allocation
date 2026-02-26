from django import forms
from .models import Room


class RoomForm(forms.ModelForm):
    class Meta:
        model = Room
        fields = ['room_no', 'capacity', 'has_ac', 'has_attached_washroom']


# 🔍 Search Form
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


# 🎯 Allocation Form
class AllocationForm(forms.Form):
    students = forms.IntegerField(min_value=1, label="Number of Students")
    needs_ac = forms.BooleanField(required=False, label="AC Required")
    needs_washroom = forms.BooleanField(required=False, label="Attached Washroom Required")