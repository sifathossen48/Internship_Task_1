# Generated by Django 4.2 on 2023-08-05 15:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0027_rename_name_service_title_remove_service_image_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='service',
            old_name='icon',
            new_name='service_logo',
        ),
    ]