# Generated by Django 4.0.5 on 2022-06-27 22:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0003_work_title_alter_work_d_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='work',
            name='title',
            field=models.TextField(max_length=50, null=True, verbose_name='Title'),
        ),
    ]
