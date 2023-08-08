# Generated by Django 4.2 on 2023-08-08 08:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0036_topclients_thumb_no'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='teammember',
            name='skill',
        ),
        migrations.AddField(
            model_name='teammember',
            name='skill',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='website.skill'),
        ),
    ]
