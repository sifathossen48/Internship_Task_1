# Generated by Django 4.2 on 2023-08-02 17:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=70)),
                ('image', models.ImageField(upload_to='projects/')),
                ('serial', models.IntegerField(unique=True)),
                ('location', models.CharField(max_length=40)),
            ],
        ),
    ]
