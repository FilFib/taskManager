# Generated by Django 4.2.6 on 2023-10-21 09:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='task',
            old_name='complate_date',
            new_name='complete_date',
        ),
    ]