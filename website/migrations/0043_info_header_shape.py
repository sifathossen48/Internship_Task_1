# Generated by Django 4.2 on 2023-08-20 09:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0042_about_about_quote_icon'),
    ]

    operations = [
        migrations.AddField(
            model_name='info',
            name='header_shape',
            field=models.ImageField(null=True, upload_to='shape/'),
        ),
    ]
