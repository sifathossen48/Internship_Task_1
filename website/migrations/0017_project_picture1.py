# Generated by Django 4.2 on 2023-08-13 10:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0016_projectitem_remove_project_category_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='picture1',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='website.projectitem'),
        ),
    ]