# Generated by Django 4.0.4 on 2022-05-10 15:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('src', '0003_note_sec_note_sem_alter_note_branch_delete_basic'),
    ]

    operations = [
        migrations.AddField(
            model_name='note',
            name='note_file',
            field=models.FileField(blank=True, null=True, upload_to='notes/'),
        ),
    ]
