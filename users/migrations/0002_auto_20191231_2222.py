# Generated by Django 2.2.5 on 2019-12-31 13:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='avatar',
            field=models.ImageField(blank=True, help_text='프로필사진', upload_to='avatars'),
        ),
    ]
