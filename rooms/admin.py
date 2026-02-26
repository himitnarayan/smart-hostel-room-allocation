from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Allocation, Room

@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
    list_display = ('room_no', 'capacity', 'has_ac', 'has_attached_washroom', 'created_at')
    search_fields = ('room_no',)
    list_filter = ('has_ac', 'has_attached_washroom')
    admin.site.register(Allocation)