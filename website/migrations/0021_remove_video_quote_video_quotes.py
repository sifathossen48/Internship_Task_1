# Generated by Django 4.2 on 2023-08-15 14:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0020_video_quote'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='video',
            name='quote',
        ),
        migrations.AddField(
            model_name='video',
            name='quotes',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='website.testimonial'),
            preserve_default=False,
        ),
    ]
