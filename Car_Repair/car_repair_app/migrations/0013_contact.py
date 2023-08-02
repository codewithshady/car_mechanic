# Generated by Django 4.1.7 on 2023-03-11 09:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('car_repair_app', '0012_career'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=254)),
                ('message', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
