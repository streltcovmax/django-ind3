from django import forms
from .models import *

class ArtistForm(forms.ModelForm):
    class Meta:
        model = Artist
        fields = ['name', 'phone']

class InstrumentForm(forms.ModelForm):
    class Meta:
        model = Instrument
        fields = ['name', 'type']

class InstructorForm(forms.ModelForm):
    class Meta:
        model = Instructor
        fields = ['name', 'phone', 'specialization']

class LessonForm(forms.ModelForm):
    lesson_date = forms.DateTimeField(
        label="Дата и время занятия",
        widget=forms.DateTimeInput(attrs={'type': 'datetime-local'})
    )

    class Meta:
        model = Lesson
        fields = ['artist', 'instrument', 'instructor', 'lesson_date']
