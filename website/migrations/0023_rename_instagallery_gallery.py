# Generated by Django 4.2 on 2023-08-15 15:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0022_instagallery'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='InstaGallery',
            new_name='Gallery',
        ),
    ]