# Generated by Django 3.2.5 on 2022-06-27 20:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api_img', '0002_remove_img_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='img',
            name='name',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
