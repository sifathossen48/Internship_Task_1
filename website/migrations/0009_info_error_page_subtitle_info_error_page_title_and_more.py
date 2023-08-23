# Generated by Django 4.2 on 2023-08-12 09:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0008_info_pinterest'),
    ]

    operations = [
        migrations.AddField(
            model_name='info',
            name='error_page_subtitle',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='info',
            name='error_page_title',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='info',
            name='error_page_title_background',
            field=models.ImageField(null=True, upload_to='background/'),
        ),
    ]