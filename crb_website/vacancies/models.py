from django.db import models


class Vacancy(models.Model):
    CATEGORY_CHOICES = [
        ('high_med_education', 'Высшее медицинское образование'),
        ('secondary_med_education', 'Среднее специальное медицинское образование'),
        ('high_education', 'Высшее не медицинское образование'),
        ('secondary_education', 'Среднее не медицинское образование'),
        ('other', 'Другое'),
    ]

    title = models.CharField(max_length=255)
    position = models.TextField(blank=True)
    is_active = models.BooleanField(default=True)
    category = models.CharField(
        max_length=30, choices=CATEGORY_CHOICES, default='secondary_med_education')

    class Meta:
        verbose_name = 'Вакансия'
        verbose_name_plural = 'Вакансии'

    def __str__(self):
        return f"{self.title} - {self.position}"
