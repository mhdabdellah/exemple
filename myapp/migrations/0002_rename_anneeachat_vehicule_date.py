# Generated by Django 3.2.3 on 2022-12-08 22:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='vehicule',
            old_name='anneeAchat',
            new_name='date',
        ),
    ]
