# Generated by Django 4.1.7 on 2023-11-15 11:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sub_cat', '0006_remove_subcat_self_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='subcat',
            name='pic_name',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
    ]
