from django.db import models

status_choices = [
    ('new', 'Новая'),
    ('in_progress', 'В процессе'),
    ('done', 'Сделано')
]


class Work(models.Model):
    new = 'nw'
    in_progress = 'i_p'
    done = 'dn'

    description = models.CharField(max_length=100, null=False, blank=False, verbose_name="Описание")
    status = models.CharField(max_length=20, choices=status_choices, default=status_choices[0][0],
                              verbose_name="Статус работы")
    d_date = models.DateField(auto_created=True, verbose_name="дата сдачи")
    title = models.TextField(max_length=50, null=True, verbose_name="Title")

    def __str__(self):
        return f"{self.pk}. {self.description} - {self.status} - {self.d_date} - {self.title}"

    class Meta:
        db_table = "works"
        verbose_name = "Задача"
        verbose_name_plural = "Задачи"
