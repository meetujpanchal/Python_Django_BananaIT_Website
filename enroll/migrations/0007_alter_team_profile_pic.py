# Generated by Django 4.0.4 on 2022-06-23 11:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('enroll', '0006_testimonial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='team',
            name='profile_pic',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
    ]
