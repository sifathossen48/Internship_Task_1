# Generated by Django 4.2 on 2023-08-08 08:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0035_topclients'),
    ]

    operations = [
        migrations.AddField(
            model_name='topclients',
            name='thumb_no',
            field=models.CharField(max_length=2, null=True),
        ),
    ]