# Generated by Django 4.2 on 2023-04-27 14:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0008_alter_book_writer_favbookcollection'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='cerated',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='book',
            name='updated',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
    ]