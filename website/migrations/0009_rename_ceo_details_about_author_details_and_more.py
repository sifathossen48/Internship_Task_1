# Generated by Django 4.2 on 2023-08-03 08:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0008_rename_item_locatio_about_item_location'),
    ]

    operations = [
        migrations.RenameField(
            model_name='about',
            old_name='ceo_details',
            new_name='author_details',
        ),
        migrations.RenameField(
            model_name='about',
            old_name='ceo_image',
            new_name='author_image',
        ),
        migrations.RenameField(
            model_name='about',
            old_name='ceo_name',
            new_name='author_name',
        ),
        migrations.AddField(
            model_name='about',
            name='author_title',
            field=models.CharField(max_length=20, null=True),
        ),
    ]
