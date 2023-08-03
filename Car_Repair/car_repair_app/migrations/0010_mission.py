# Generated by Django 4.1.7 on 2023-03-04 09:35

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('car_repair_app', '0009_about_description3'),
    ]

    operations = [
        migrations.CreateModel(
            name='Mission',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('details', ckeditor.fields.RichTextField()),
                ('details1', ckeditor.fields.RichTextField()),
                ('details2', ckeditor.fields.RichTextField()),
            ],
        ),
    ]
