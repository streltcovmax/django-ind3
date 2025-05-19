from django.contrib import admin
from .models import *

@admin.register(Artist)
class ArtistAdmin(admin.ModelAdmin):
    list_display = ['name', 'phone']
    search_fields = ['name', 'phone']

@admin.register(Instrument)
class InstrumentAdmin(admin.ModelAdmin):
    list_display = ['name', 'type']
    list_filter = ['type']
    search_fields = ['name']

@admin.register(Instructor)
class InstructorAdmin(admin.ModelAdmin):
    list_display = ['name', 'phone', 'specialization']
    list_filter = ['specialization']
    search_fields = ['name', 'specialization']

@admin.register(Lesson)
class LessonAdmin(admin.ModelAdmin):
    list_display = ['artist', 'instructor', 'instrument', 'lesson_date']
    list_filter = ['lesson_date', 'instructor']
