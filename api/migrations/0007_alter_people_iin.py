# Generated by Django 4.0.1 on 2022-01-27 10:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0006_people'),
    ]

    operations = [
        migrations.AlterField(
            model_name='people',
            name='iin',
            field=models.CharField(max_length=12, unique=True, verbose_name='ИИН'),
        ),
    ]
