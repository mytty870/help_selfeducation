# Generated by Django 3.2.3 on 2021-06-26 14:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('postsite', '0002_user_icon'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='icon',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]