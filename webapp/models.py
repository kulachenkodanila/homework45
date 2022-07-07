from django.db import models

status_choices = [
    ('new', 'Новая'),
    ('in_progress', 'В процессе'),
    ('done', 'Сделано')
]


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Дата изменения")

    class Meta:
        abstract = True


class Status(BaseModel):
    status = models.CharField(max_length=100, null=True, blank=True, verbose_name="Статус")

    def __str__(self):
        return f"{self.pk}. {self.summary} - {self.status}"

    class Meta:
        db_table = "Statuses"
        verbose_name = "Статус"
        verbose_name_plural = "Статусы"


class Type(BaseModel):
    type = models.CharField(max_length=100, null=True, blank=True, verbose_name="Тип")

    def __str__(self):
        return f"{self.pk}. {self.summary} - {self.type}"

    class Meta:
        db_table = "Types"
        verbose_name = "Тип"
        verbose_name_plural = "Типы"


class Work(BaseModel):
    summary = models.CharField(max_length=100, null=False, blank=False, verbose_name="Заголовок")
    description = models.TextField(max_length=100, null=True, blank=True, verbose_name="Описание")
    status = models.ForeignKey("webapp.Work", on_delete=models.CASCADE, related_name="Statuses", verbose_name="Статус")
    type = models.ForeignKey("webapp.Work", on_delete=models.CASCADE, related_name="Types", verbose_name="Тип")

    def __str__(self):
        return f"{self.pk}. {self.description} - {self.status} - {self.summary} - {self.type}"

    class Meta:
        db_table = "works"
        verbose_name = "Задача"
        verbose_name_plural = "Задачи"
