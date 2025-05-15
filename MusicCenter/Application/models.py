from django.db import models
from django.core.validators import RegexValidator

phone_validator = RegexValidator(
    regex=r'^\+7\d{10}$',
    message='Введите номер в формате +7XXXXXXXXXX (11 цифр)'
)

class Artist(models.Model):
    name = models.CharField(max_length=70, verbose_name="Имя артиста")
    phone = models.CharField(max_length=15, verbose_name="Телефон", validators=[phone_validator])

    required_fields = ['name']

    class Meta:
        verbose_name = "артист"
        verbose_name_plural = "артисты"

    def __str__(self):
        return f"{self.name}"

class Instrument(models.Model):
    class Type(models.TextChoices):
        STRING = 'Струнный', 'Струнный'
        WIND = 'Духовой', 'Духовой'
        PERCUSSION = 'Ударный', 'Ударный'
        OTHER = 'Иной', 'Иной'

    # artist = models.ForeignKey(Artist, on_delete=models.CASCADE, verbose_name="Артист")
    name = models.CharField(max_length=50, verbose_name="Название инструмента")
    type = models.CharField(max_length=50, verbose_name="Тип", choices=Type.choices, default=Type.OTHER)

    required_fields = ['name', 'type']

    class Meta:
        verbose_name = "инструмент"
        verbose_name_plural = "инструменты"

    def __str__(self):
        return f"{self.name} ({self.type})"

class Instructor(models.Model):
    name = models.CharField(max_length=70, verbose_name="Имя инструктора")
    phone = models.CharField(max_length=15, verbose_name="Телефон", validators=[phone_validator])
    specialization = models.CharField(max_length=150, verbose_name="Специализация")

    required_fields = ['name']

    class Meta:
        verbose_name = "инструктор"
        verbose_name_plural = "инструкторы"

    def __str__(self):
        return f"{self.name}"

class Lesson(models.Model):
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE, verbose_name="Артист")
    instructor = models.ForeignKey(Instructor, on_delete=models.CASCADE, verbose_name="Инструктор")
    instrument = models.ForeignKey(Instrument, on_delete=models.CASCADE, verbose_name="Инструмент")
    lesson_date = models.DateTimeField(verbose_name="Дата и время занятия")

    required_fields = ['artist', 'instructor', 'instrument', 'lesson_date']

    class Meta:
        verbose_name = "занятие"
        verbose_name_plural = "занятия"
