# Generated by Django 4.2 on 2023-05-18 05:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='datecompleted',
            field=models.DateField(blank=True, null=True),
        ),
    ]
