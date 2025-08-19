from django.db import models


class Specialist(models.Model):
    CATEGORY_CHOICES = [
        ('admin', 'Администрация'),
        ('general', 'Специалисты на странице "Специалисты"'),
        ('schedule_specialists', 'Специалисты в графике приёма'),
    ]

    name = models.CharField(max_length=255)
    position = models.CharField(max_length=255)
    photo = models.ImageField(upload_to='staff_photos/', blank=True, null=True)
    bio = models.TextField(blank=True)
    is_active = models.BooleanField(default=True)
    phone = models.CharField(max_length=30, blank=True)
    category = models.CharField(
        max_length=20, choices=CATEGORY_CHOICES, default='general')
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order']
        verbose_name = 'Специалиста'
        verbose_name_plural = 'Специалисты'

    def __str__(self):
        return f"{self.name} - {self.position}"
