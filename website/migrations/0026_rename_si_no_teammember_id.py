# Generated by Django 4.2 on 2023-08-05 10:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0025_remove_service_html_file'),
    ]

    operations = [
        migrations.RenameField(
            model_name='teammember',
            old_name='si_no',
            new_name='id',
        ),
    ]
