# Generated by Django 2.1.5 on 2019-01-26 06:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('share2go', '0003_note_note_created_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='note',
            name='note_created_date',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]