# Generated by Django 4.0.1 on 2022-01-27 05:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_alter_user_number_house_alter_user_street'),
    ]

    operations = [
        migrations.CreateModel(
            name='People',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('iin', models.CharField(max_length=12, verbose_name='ИИН')),
            ],
        ),
    ]