from django.db import models


class Work(models.Model):
    new = 'nw'
    in_progress = 'i_p'
    done = 'dn'
    status_choices = [
        ('new', 'Новая'),
        ('in_progress', 'В процессе'),
        ('done', 'Сделано')
    ]
    description = models.CharField(max_length=100, null=False, blank=False, verbose_name="Описание")
    status = models.CharField(max_length=2, choices=status_choices, default=new, verbose_name="Статус работы")
    d_date = models.DateField(auto_created=False, verbose_name="дата сдачи")

    def __str__(self):
        return f"{self.id}. {self.description} - {self.status} - {self.d_date}"