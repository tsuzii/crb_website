from django.db import models


class Schedule(models.Model):
    class Location(models.TextChoices):
        DISTRICT_THERAPISTS = "therapists", "Терапевтическая участковая служба"
        DISTRICT_PEDIATRICIANS = "pediatricians", "Педиатрическая участковая служба"
        POLYCLINIC = "polyclinic", "Поликлиника"
        IVENEC = "ivenec", "Ивенецкая горпоселковая больница"
        RAKOV = "rakov", "Раковская участковая больница"

    name = models.CharField('Ф.И.О. сотрудника', max_length=100)
    speciality = models.CharField('Специальность', max_length=100)
    location = models.CharField(
        "Место приёма",
        max_length=20,
        choices=Location.choices,
        default=Location.POLYCLINIC,
    )

    monday = models.CharField(
        'Понедельник', max_length=50, blank=True, null=True)
    tuesday = models.CharField('Вторник', max_length=50, blank=True, null=True)
    wednesday = models.CharField('Среда', max_length=50, blank=True, null=True)
    thursday = models.CharField(
        'Четверг', max_length=50, blank=True, null=True)
    friday = models.CharField('Пятница', max_length=50, blank=True, null=True)

    class Meta:
        verbose_name = "График специалиста"
        verbose_name_plural = "Графики специалистов"

    def __str__(self):
        return f"{self.name} ({self.speciality})"
