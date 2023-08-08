# Generated by Django 4.2 on 2023-08-03 06:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0004_preloader'),
    ]

    operations = [
        migrations.CreateModel(
            name='LatestNews',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author', models.CharField(max_length=30)),
                ('timestamp', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(max_length=60)),
                ('desc', models.TextField(blank=True, null=True)),
            ],
        ),
    ]