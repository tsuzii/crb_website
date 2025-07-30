from django.db import models

# Create your models here.


class Articles(models.Model):
    title = models.CharField('Название', max_length=50,
                             default='Внеочередное новостное событие')
    img = models.ImageField(
        'Изображение', upload_to='articles/', blank=True, null=True)
    full_text = models.TextField('Статья')
    date = models.DateField('Дата публикации')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'
