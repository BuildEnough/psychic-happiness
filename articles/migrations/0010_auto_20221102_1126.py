# Generated by Django 3.2.13 on 2022-11-02 02:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0009_auto_20221102_1124'),
    ]

    operations = [
        migrations.RenameField(
            model_name='articles',
            old_name='image',
            new_name='image1',
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to='image')),
                ('article', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='articles.articles')),
            ],
        ),
    ]
