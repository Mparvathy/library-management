# Generated by Django 5.1 on 2024-09-14 12:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_book_is_issued'),
    ]

    operations = [
        migrations.AddField(
            model_name='bookissue',
            name='fine_paid',
            field=models.BooleanField(default=False),
        ),
    ]