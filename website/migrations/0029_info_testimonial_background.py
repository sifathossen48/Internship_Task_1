# Generated by Django 4.2 on 2023-08-16 08:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0028_info_project_background'),
    ]

    operations = [
        migrations.AddField(
            model_name='info',
            name='testimonial_background',
            field=models.ImageField(null=True, upload_to='background/'),
        ),
    ]
