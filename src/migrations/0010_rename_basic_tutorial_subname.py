# Generated by Django 4.0.4 on 2022-05-24 15:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('src', '0009_note_nname'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tutorial',
            old_name='basic',
            new_name='subname',
        ),
    ]