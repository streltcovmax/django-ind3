from django.shortcuts import render, get_object_or_404, redirect
from .forms import *
import datetime

def CreateFromForm(request, form_model, title):
    form = form_model(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect(f'/{form_model.Meta.model.__name__}/view')
    return render(request, 'update.html', {'form': form, 'title': title})


def ArtistCreate(request):
    return CreateFromForm(request, ArtistForm, "Создать артиста")


def InstrumentCreate(request):
    return CreateFromForm(request, InstrumentForm, "Создать инструмент")


def InstructorCreate(request):
    return CreateFromForm(request, InstructorForm, "Создать инструктора")


def LessonCreate(request):
    return CreateFromForm(request, LessonForm, "Создать занятие")


def EditFromForm(request, pk, form_model, title):
    model = get_object_or_404(form_model.Meta.model, pk=pk)
    form = form_model(request.POST or None, instance=model)
    if form.is_valid():
        form.save()
        return redirect(f'/{form_model.Meta.model.__name__}/{pk}/detail')
    return render(request, 'update.html', {'form': form, 'title': title})


def ArtistEdit(request, pk):
    return EditFromForm(request, pk, ArtistForm, 'Изменить артиста')


def InstrumentEdit(request, pk):
    return EditFromForm(request, pk, InstrumentForm, 'Изменить инструмент')


def InstructorEdit(request, pk):
    return EditFromForm(request, pk, InstructorForm, 'Изменить инструктора')


def LessonEdit(request, pk):
    return EditFromForm(request, pk, LessonForm, 'Изменить занятие')


def DetailFromForm(request, pk, Model, title):
    model = get_object_or_404(Model, pk=pk)
    fields = [(field.verbose_name, getattr(model, field.name)) for field in model._meta.fields]
    return render(request, 'detail.html', {'fields': fields, 'title': title})


def ArtistDetail(request, pk):
    return DetailFromForm(request, pk, Artist, 'Детали артиста')


def InstrumentDetail(request, pk):
    return DetailFromForm(request, pk, Instrument, 'Детали инструмента')


def InstructorDetail(request, pk):
    return DetailFromForm(request, pk, Instructor, 'Детали инструктора')


def LessonDetail(request, pk):
    return DetailFromForm(request, pk, Lesson, 'Детали занятия')


def ViewFromForm(request, Model, title):
    queryset = Model.objects.all()
    required = getattr(Model, 'required_fields', [])
    fields = [Model._meta.get_field(field_name).verbose_name for field_name in required]
    objects = []
    for el in queryset:
        obj = [getattr(el, 'id')]
        for field_name in required:
            val = getattr(el, field_name)
            if not isinstance(val, (datetime.date, datetime.datetime)):
                val = str(val)
            obj.append(val)
        objects.append(obj)

    return render(request, 'list.html', {
        'title': title,
        'fields': fields,
        'objects': objects,
        'model_name': Model.__name__
    })


def ArtistView(request):
    return ViewFromForm(request, Artist, "Артисты")


def InstrumentView(request):
    return ViewFromForm(request, Instrument, "Инструменты")


def InstructorView(request):
    return ViewFromForm(request, Instructor, "Инструкторы")


def LessonView(request):
    return ViewFromForm(request, Lesson, "Занятия")