# Generated by Django 4.2 on 2023-08-12 07:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0007_alter_latestnews_category_delete_blogcategory'),
    ]

    operations = [
        migrations.AddField(
            model_name='info',
            name='pinterest',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
    ]
