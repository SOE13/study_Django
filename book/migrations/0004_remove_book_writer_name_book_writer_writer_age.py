# Generated by Django 4.2 on 2023-04-23 13:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0003_writer'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='writer_name',
        ),
        migrations.AddField(
            model_name='book',
            name='writer',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='book.writer'),
        ),
        migrations.AddField(
            model_name='writer',
            name='age',
            field=models.CharField(max_length=2, null=True),
        ),
    ]
