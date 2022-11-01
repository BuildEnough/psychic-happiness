# Generated by Django 3.2.13 on 2022-11-01 07:55

from django.db import migrations
import imagekit.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_profile_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='thumbnail',
            field=imagekit.models.fields.ProcessedImageField(blank=True, upload_to='images/'),
        ),
    ]
