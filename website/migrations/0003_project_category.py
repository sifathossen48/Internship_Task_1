# Generated by Django 4.2 on 2023-08-10 19:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0002_about_client_comingsoon_comment_contact_contactus_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='website.projecttype'),
        ),
    ]
