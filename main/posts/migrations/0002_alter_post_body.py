# Generated by Django 5.1 on 2024-08-26 10:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='body',
            field=models.TextField(max_length=500),
        ),
    ]
