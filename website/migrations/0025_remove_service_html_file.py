# Generated by Django 4.2 on 2023-08-05 09:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0024_info_about_title_background'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='service',
            name='html_file',
        ),
    ]