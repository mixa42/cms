from django.db import models
from django.utils.translation import gettext_lazy as _

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
        verbose_name = _('visible'),
        choices = CHOICES_VISIBLE,
        default = CHOICES_VISIBLE[0][0],
    )
    status = models.CharField(
        max_length=24,
        default='published'
    )
   
    #parent = models.ForeignKey('Menu', on_delete=models.PROTECT)

    def __str__(self):
        return str(self.name)

    class Meta:
        ordering = ('position',)
        verbose_name = 'Пункт меню'
        verbose_name_plural ='Пункты меню'