# Generated by Django 4.1.7 on 2023-02-22 01:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('category', '0002_show'),
    ]

    operations = [
        migrations.AlterField(
            model_name='show',
            name='show',
            field=models.CharField(choices=[('FR', 'Freshman'), ('SO', 'Sophomore'), ('JR', 'Junior')], max_length=15),
        ),
    ]
