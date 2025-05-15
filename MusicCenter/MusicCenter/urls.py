from django.contrib import admin
from django.urls import path
from Application import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.LessonView, name='LessonView'),

    path('Artist/create/', views.ArtistCreate, name='ArtistCreate'),
    path('Artist/<int:pk>/edit/', views.ArtistEdit, name='ArtistEdit'),
    path('Artist/<int:pk>/detail/', views.ArtistDetail, name='ArtistDetail'),
    path('Artist/view/', views.ArtistView, name='ArtistView'),

    path('Instrument/create/', views.InstrumentCreate, name='InstrumentCreate'),
    path('Instrument/<int:pk>/edit/', views.InstrumentEdit, name='InstrumentEdit'),
    path('Instrument/<int:pk>/detail/', views.InstrumentDetail, name='InstrumentDetail'),
    path('Instrument/view/', views.InstrumentView, name='InstrumentView'),

    path('Instructor/create/', views.InstructorCreate, name='InstructorCreate'),
    path('Instructor/<int:pk>/edit/', views.InstructorEdit, name='InstructorEdit'),
    path('Instructor/<int:pk>/detail/', views.InstructorDetail, name='InstructorDetail'),
    path('Instructor/view/', views.InstructorView, name='InstructorView'),

    path('Lesson/create/', views.LessonCreate, name='LessonCreate'),
    path('Lesson/<int:pk>/edit/', views.LessonEdit, name='LessonEdit'),
    path('Lesson/<int:pk>/detail/', views.LessonDetail, name='LessonDetail'),
    path('Lesson/view/', views.LessonView, name='LessonView'),
]
