from django.db import models
from django.utils.translation import gettext_lazy as _
import datetime

CHOICES_VISIBLE = [
    ('1', _('Yes')),
    ('0', _('No')),
]

class Menu(models.Model):
    name = models.CharField('Название', max_length=100)
    url = models.CharField('Ссылка', max_length=255)
    position = models.PositiveIntegerField('Позиция', default=1)

    visible = models.CharField(
        max_length = 2,
        verbose_name = _('Видимость'),
        choices = CHOICES_VISIBLE,
        default = CHOICES_VISIBLE[0][0],
    )
    
    timestamp = models.DateTimeField(default=datetime.datetime.now())
    parent = models.ForeignKey('Menu', on_delete=models.SET_NULL, blank=True, null=True, default=None, verbose_name='Родительский элемент')

    def __str__(self):
        return str(self.name)

    class Meta:
        ordering = ('position',)
        verbose_name = 'Пункт меню'
        verbose_name_plural ='Пункты меню'