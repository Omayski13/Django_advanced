# Generated by Django 5.0.2 on 2024-02-28 14:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('objects_posts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='description',
            field=models.TextField(max_length=500),
        ),
    ]
