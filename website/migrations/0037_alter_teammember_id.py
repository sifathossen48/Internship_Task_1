# Generated by Django 4.2 on 2023-08-19 08:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0036_remove_project_serial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teammember',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]