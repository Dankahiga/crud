# Generated by Django 4.2 on 2023-04-19 05:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crudapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='email',
            field=models.EmailField(max_length=254, null=True),
        ),
        migrations.AlterModelTable(
            name='student',
            table='student',
        ),
    ]
