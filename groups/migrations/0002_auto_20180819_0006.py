# Generated by Django 2.0.5 on 2018-08-18 18:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('groups', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='group',
            old_name='desciption',
            new_name='description',
        ),
    ]
