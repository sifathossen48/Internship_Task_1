# Generated by Django 4.2 on 2023-08-12 19:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0014_erroremail'),
    ]

    operations = [
        migrations.AlterField(
            model_name='erroremail',
            name='email',
            field=models.EmailField(max_length=50, unique=True),
        ),
    ]