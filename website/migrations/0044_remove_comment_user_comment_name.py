# Generated by Django 4.2 on 2023-08-22 17:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0043_info_header_shape'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='user',
        ),
        migrations.AddField(
            model_name='comment',
            name='name',
            field=models.CharField(default=1, max_length=20),
            preserve_default=False,
        ),
    ]