# Generated by Django 4.2 on 2023-08-04 16:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0015_contact'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='contact_desc',
            field=models.TextField(blank=True, null=True),
        ),
    ]
