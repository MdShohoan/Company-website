# Generated by Django 3.1.1 on 2020-10-08 07:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app2', '0002_service'),
    ]

    operations = [
        migrations.CreateModel(
            name='portfolio',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField(max_length=700)),
                ('image', models.ImageField(upload_to='portfolio')),
            ],
        ),
    ]
